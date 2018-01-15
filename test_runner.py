import Image
import zxing_fast
# from zxing_fast import tag_reader
import os


def main():
    # tag_reader.setup(["C:/users/david/PycharmProjects/python-zxing-fast/jars/core.jar",
    #                       "C:/users/david/PycharmProjects/python-zxing-fast/jars/javase.jar"],
    #                  java_home="C:/Program Files/Java/jre1.8.0_74",
    #                  jdk_home="C:/Program Files/Java/jdk1.8.0_74")
    # tag_reader.setup(["C:/users/david/PycharmProjects/python-zxing-fast/jars/core.jar",
    #                   "C:/users/david/PycharmProjects/python-zxing-fast/jars/javase.jar"],
    #                  java_home="C:/Program Files/Java/jdk1.8.0_74")
    # print tag_reader.read_tag(Image.open("duckiebot successful.png"))

    if os.name == "nt":
        reader = zxing_fast.BarcodeReader(["C:/users/david/PycharmProjects/python-zxing-fast/jars/core.jar",
                                           "C:/users/david/PycharmProjects/python-zxing-fast/jars/javase.jar"],
                                          java_home="C:/Program Files/Java/jre1.8.0_74/bin/server")
    else:
        reader = zxing_fast.BarcodeReader(
            "/home/david/Documents/14_algorithmic_robotics/src/ar_tags/include/zxing/javase/target/"
            "javase-3.3.2-SNAPSHOT.jar:/home/david/Documents/14_algorithmic_robotics/src/ar_tags/"
            "include/zxing/core/core.jar", java_home="/usr/lib/jvm/default-java")

    print reader.read_tag(Image.open("duckiebot successful.png"))
    print reader.read_tag(Image.open("C:/users/david/Downloads/qrcode.png"))
    print reader.read_tag(Image.open("C:/users/david/Downloads/qrcode (1).png"))


if __name__ == "__main__":
    main()
