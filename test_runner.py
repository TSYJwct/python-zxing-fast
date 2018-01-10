import Image
from zxing_fast import tag_reader


def main():

    img = Image.open("duckiebot successful.png")

    tag_reader.setup("/home/david/Documents/14_algorithmic_robotics/src/ar_tags/include/zxing/javase/target/"
                     "javase-3.3.2-SNAPSHOT.jar:/home/david/Documents/14_algorithmic_robotics/src/ar_tags/"
                     "include/zxing/core/core.jar", "/usr/lib/jvm/default-java")

    print tag_reader.read_tag(img)


if __name__ == "__main__":
    main()
