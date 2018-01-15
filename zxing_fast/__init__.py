from __future__ import print_function
import os
import io


class BarcodeReader:

    def __init__(self, classpath, java_home=None):
        if java_home is not None:
            os.environ['JAVA_HOME'] = java_home
        # os.environ['CLASSPATH'] = classpath
        import jnius_config
        for path in classpath:
            jnius_config.add_classpath(path)

        from jnius import autoclass  # import jnius here so that CLASSPATH and JAVA_HOME can be set beforehand
        self.ByteArrayInputStream = autoclass('java.io.ByteArrayInputStream')
        self.ImageIO = autoclass('javax.imageio.ImageIO')
        self.ByteBuffer = autoclass('java.nio.ByteBuffer')
        self.BufferedImageLuminanceSource = autoclass('com.google.zxing.client.j2se.BufferedImageLuminanceSource')
        self.HybridBinarizer = autoclass('com.google.zxing.common.HybridBinarizer')
        self.BinaryBitmap = autoclass('com.google.zxing.BinaryBitmap')
        self.MultiFormatReader = autoclass('com.google.zxing.MultiFormatReader')

    def read_tag(self, image):
        output = io.BytesIO()
        image.save(output, 'png')
        serialized_img = output.getvalue()
        output.close()

        # convert python PIL image to a java BufferedImage
        byteArray = self.ByteBuffer.wrap(serialized_img)
        byteInputStream = self.ByteArrayInputStream(byteArray.array())

        imageInputStream = self.ImageIO.createImageInputStream(byteInputStream)
        bufferedImage = self.ImageIO.read(imageInputStream)

        source = self.BufferedImageLuminanceSource(bufferedImage)
        bitmap = self.BinaryBitmap(self.HybridBinarizer(source))
        reader = self.MultiFormatReader()

        resultJava = reader.decode(bitmap)
        result_python = BarCode()
        result_python.raw = resultJava.getText()
        result_python.points = resultJava.getResultPoints()
        result_python.format = resultJava.getBarcodeFormat()


class BarCode:
    """
    Designed to be compatible with the BarCode class provided by Python-Zxing
    (github.com/oostendo/python-zxing)
    """
    def __init__(self):
        self.format = ""
        self.raw = ""
        self.data = ""
        self.points = []

    def __str__(self):
        return self.data
