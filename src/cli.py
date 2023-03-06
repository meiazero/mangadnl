import os
import sys
import argparse
import logging
from dnl import GetAllLinksImages, Downloader


class DownloaderMangar():

    CLI_VERSION = "0.0.1"

    def __init__(self):
        self.__run()

    def __run(self):

        self.parser = argparse.ArgumentParser(
            prog="downloader-mangar",
            description="Download manga from hubmanga.com",
            epilog="Made with love by @meiazero",
            usage="%(prog)s [options]")

        self.parser.version = self.CLI_VERSION

        self.parser.add_argument("-v", "--version", action="version")

        self.parser.add_argument(
            "-m", "--manga", type=str, default="", required=True, help="Manga name")

        self.parser.add_argument(
            "-n", "--name", type=str, default="", required=False, help="Optional name of the manga")

        self.parser.add_argument(
            "-c", "--chapter", type=int, default=1, required=True, help="Number of chapter")

        self.parser.add_argument(
            "-d", "--dir", type=str, default=".", required=False, help="Directory to save the manga (deprecated))")

        args_parser = self.__args()

        if args_parser:
            try:
                if args_parser.manga != "":
                    name_manga = f"hubmanga.com/manga/{args_parser.manga}"
                else:
                    print("Manga name is required")
                    sys.exit(1)

                if args_parser.name != "":
                    alias_name_manga = f"{args_parser.name}"
                else:
                    alias_name_manga = ""

                if args_parser.chapter != 0:
                    if args_parser.chapter > 0:
                        num_chapter = args_parser.chapter
                    else:
                        print("Chapter must be greater than 0")
                        sys.exit(1)
                else:
                    num_chapter = 1

                f_url = f"https://{name_manga}-chapter-{num_chapter}"
                print(f"full url: {f_url}\n")

                _urls = GetAllLinksImages(f_url)
                # print(_urls)

                try:
                    if alias_name_manga != "":
                        Downloader(
                            _urls, alias_name_manga, num_chapter)
                    else:
                        Downloader(
                            _urls, args_parser.manga, num_chapter)
                except Exception as e:
                    print(e)
                    sys.exit(1)

            except Exception as e:
                os.makedirs("logs", exist_ok=True)
                logging.basicConfig(
                    level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='logs/downloader-mangar.log')
                logging.error("Error: {}".format(e))

    def __args(self):
        return self.parser.parse_args()
