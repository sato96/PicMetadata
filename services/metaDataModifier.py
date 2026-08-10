"""
This class provides four main functionalities for batch image metadata editing:

1) Automatic mode: processes all images where the date can be inferred from
   known filename patterns. Images that do not match any known pattern are skipped.

2) Manual mode: iterates over all images that require a date, displays each one
   to the user and waits for manual date input before moving to the next.

3) Single image mode: displays a user-selected image, prompts for a date and
   applies it by calling change_date() directly. Intended for one-off corrections.

4) Hybrid mode: combines modes 1 and 2 in a sequential pipeline.
   First runs automatic processing on all images with known patterns,
   then switches to manual mode for the remaining ones.
   Compared to pure manual mode (2), the user is prompted less frequently
   since images with a valid date or a recognized pattern are skipped automatically.
"""

import os
from pathlib import Path
from PIL import Image
import piexif
from datetime import datetime


class metaDataModifier(object):

    def __init__(self, folder):
        self.__check_folder(folder)
        self.__modalities = ('full', 'manual', 'auto', 'analysis')

    def __check_folder(self, folder):
        if not isinstance(folder, str):
            raise TypeError(f"'folder' must be a string, got: {type(folder).__name__}")
        path = Path(folder)
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: '{folder}'")
        if not path.is_dir():
            raise NotADirectoryError(f"Path exists but is not a directory: '{folder}'")
        if not os.access(path, os.R_OK):
            raise PermissionError(f"No read permission on directory: '{folder}'")
        self.__folder = path

    @property
    def folder(self):
        return self.__folder

    @folder.setter
    def folder(self, folder):
        self.__check_folder(folder)

    def __is_file(self, imgPath):
        return os.path.isfile(imgPath)

    def get_exif_data(self, imgPath):
        try:
            img = Image.open(imgPath)
            return img.getexif()
        except:
            return None

    def __define_date(self, imgName):
        try:
            if "WA" in imgName:
                compressDate = imgName.split("-")[1]
                date = datetime.strptime(compressDate, "%Y%m%d").date()
            elif "WIN" in imgName:
                compressDate = imgName.split("WIN_")[1].split("_PRO")[0].replace("_", "")
                date = datetime.strptime(compressDate, "%Y%m%d%H%M%S").date()
            elif "IMG" in imgName:
                compressDate = imgName.split("_")[1]
                date = datetime.strptime(compressDate, "%Y%m%d").date()
            else:
                return None
            return date.strftime("%Y:%m:%d %H:%M:%S")
        except Exception:
            return None

    def change_date(self, imgPath, newDate=None):
        img = Image.open(imgPath)
        exif_data_raw = img.info.get("exif")
        if exif_data_raw is None:
            exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
        else:
            exif_dict = piexif.load(exif_data_raw)
        new_date_bytes = newDate.encode("utf-8")
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = new_date_bytes
        exif_dict["Exif"][piexif.ExifIFD.DateTimeDigitized] = new_date_bytes
        exif_dict["0th"][piexif.ImageIFD.DateTime] = new_date_bytes
        try:
            exif_bytes = piexif.dump(exif_dict)
            img.save(imgPath, exif=exif_bytes)
        except Exception as e:
            raise Exception(f"Saving error of '{imgPath}': {e}")
        finally:
            img.close()

    def folder_analysis(self, mode='full', callback=None, manual_request=None):
        """
        manual_request: callable(imgPath) -> str | None
            Chiamato quando un'immagine richiede input manuale.
            Restituisce la data in formato "YYYY:MM:DD HH:MM:SS" oppure None se skippata.
            ATTENZIONE: questa funzione BLOCCA finché l'utente non risponde.
            Deve essere thread-safe (usa threading.Event internamente nel controller).
        """
        status = {
            "current_data": {"current_image": "", "fl_manual": False},
            "analysis": {
                "nrImages": 0,
                "current_percentage": 0,
                "images_fixed": 0,
                "images_manual_fix": 0,
                "images_skipped": 0,
                "img_no_data": 0
            }
        }

        if mode not in self.__modalities:
            raise Exception(f"Invalid mode '{mode}'")

        included_extensions = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
        files = [fn for fn in os.listdir(self.__folder)
                 if any(fn.lower().endswith(ext) for ext in included_extensions)]

        countFixed = 0
        countManual = 0
        countSkipped = 0
        countNoData = 0
        countFiles = len(files)

        if countFiles == 0:
            return status

        status["analysis"]["nrImages"] = countFiles

        for i, file in enumerate(files, start=1):
            imgPath = os.path.join(self.__folder, file)

            if not self.__is_file(imgPath):
                continue

            status["current_data"]["current_image"] = imgPath
            status["current_data"]["fl_manual"] = False

            data = self.get_exif_data(imgPath)
            if data is not None and 306 not in data.keys():
                # Immagine senza data
                countNoData += 1

                if mode == 'analysis':
                    pass  # solo conta, non tocca nulla

                elif mode == 'auto':
                    dateNew = self.__define_date(file)
                    if dateNew is not None:
                        self.change_date(imgPath, dateNew)
                        countFixed += 1

                elif mode == 'manual':
                    status["current_data"]["fl_manual"] = True
                    if manual_request:
                        dateNew = manual_request(imgPath)  # ← BLOCCA qui
                        if dateNew is not None:
                            self.change_date(imgPath, dateNew)
                            countManual += 1
                        else:
                            countSkipped += 1

                elif mode == 'full':
                    dateNew = self.__define_date(file)
                    if dateNew is not None:
                        # Auto: pattern riconosciuto
                        self.change_date(imgPath, dateNew)
                        countFixed += 1
                    else:
                        # Manuale: pattern non riconosciuto
                        status["current_data"]["fl_manual"] = True
                        if manual_request:
                            dateNew = manual_request(imgPath)  # ← BLOCCA qui
                            if dateNew is not None:
                                self.change_date(imgPath, dateNew)
                                countManual += 1
                            else:
                                countSkipped += 1

            # Aggiorna percentuale
            perc = i / countFiles * 100
            status["analysis"]["current_percentage"] = perc
            status["analysis"]["images_fixed"] = countFixed
            status["analysis"]["images_manual_fix"] = countManual
            status["analysis"]["images_skipped"] = countSkipped
            status["analysis"]["img_no_data"] = countNoData

            if callback:
                callback(status)

        status["analysis"]["current_percentage"] = 100
        return status

