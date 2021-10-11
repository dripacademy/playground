import shutil
from os import makedirs
from datetime import datetime
from pathlib import Path
from typing import Optional

import requests

# url is formatted as follows
# https://storage.roundshot.com/5595515f75aba9.83008277/2021-10-11/10-10-00/2021-10-11-10-10-00_full.jpg


def create_folders(dt: datetime) -> Path:
    p = Path(f"{dt.year}-{dt.month}") / Path(str(dt.day))
    makedirs(p, exist_ok=True)

    return p


def normalize_minute(dt: datetime) -> datetime:
    # image only taken in 10 minute intervals
    return dt.replace(minute=dt.minute - (dt.minute % 10))


def create_url(dt: datetime):

    pre_url = "https://storage.roundshot.com/5595515f75aba9.83008277"
    date_fragment = f"{dt.year}-{dt.month}-{dt.day}"
    time_fragment = f"{dt.hour}-{dt.minute}-00"

    # stitching the url together
    # of course, we also want the highest resolution
    full_url = f"{pre_url}/{date_fragment}/{time_fragment}/{date_fragment}-{time_fragment}_full.jpg"

    return full_url


def make_request(url: str) -> Optional[requests.Response]:
    res = requests.get(url, stream=True)

    if res.status_code != 200:
        return None

    return res


def save_image(res: requests.Response, path: Path, minute):
    img_path = Path(path / f"{minute}.jpg")

    with open(img_path, mode="wb") as img:
        shutil.copyfileobj(res.raw, img)

    print(f"Successfully saved Image in '{img_path}'.")


def main():
    # no arguments, just scrape most recent image
    now = datetime.now()
    now = normalize_minute(now)

    url = create_url(now)

    res = make_request(url)

    if res is not None:
        path = create_folders(now)

        save_image(res, path, now.minute)
    else:
        print("Latest Image could not be fetched.\nTrying last Image.")

        if now.minute - 10 < 0:
            now = now.replace(minute=50)
        else:
            now = now.replace(minute=now.minute - 10)

        url = create_url(now)

        res = make_request(url)

        path = create_folders(now)
        save_image(res, path, now.minute)


if __name__ == "__main__":
    main()
