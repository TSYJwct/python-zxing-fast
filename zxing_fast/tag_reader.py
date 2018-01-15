from __future__ import print_function
import os
import io


def setup(classpath, java_home=None):
    if java_home is not None:
        os.environ['JAVA_HOME'] = java_home
    # os.environ['CLASSPATH'] = classpath
    # os.environ['PATH'] = "C:\Program Files\Java\jre1.8.0_74\bin\server;" + os.environ['PATH']
    import jnius_config
    for i in classpath:
        jnius_config.add_classpath(i)


def read_tag(image):
    output = io.BytesIO()
    image.save(output, 'png')
    serialized_img = output.getvalue()
    output.close()

    # convert python PIL image to a java BufferedImage
    from jnius import autoclass  # import jnius here so that CLASSPATH and JAVA_HOME can be set beforehand
    ByteArrayInputStream = autoclass('java.io.ByteArrayInputStream')
    ImageIO = autoclass('javax.imageio.ImageIO')
    ByteBuffer = autoclass('java.nio.ByteBuffer')
    BufferedImageLuminanceSource = autoclass('com.google.zxing.client.j2se.BufferedImageLuminanceSource')
    HybridBinarizer = autoclass('com.google.zxing.common.HybridBinarizer')
    BinaryBitmap = autoclass('com.google.zxing.BinaryBitmap')
    MultiFormatReader = autoclass('com.google.zxing.MultiFormatReader')

    byteArray = ByteBuffer.wrap(serialized_img)
    imageByteArray = byteArray.array()
    byteInputStream = ByteArrayInputStream(imageByteArray)

    imageInputStream = ImageIO.createImageInputStream(byteInputStream)
    bufferedImage = ImageIO.read(imageInputStream)

    source = BufferedImageLuminanceSource(bufferedImage)
    bitmap = BinaryBitmap(HybridBinarizer(source))
    reader = MultiFormatReader()

    result = reader.decode(bitmap)
    text = result.getText()



class BarCode:
    '''
    Designed to be a drop-in replacement for the BarCode class provided by Python-Zxing
    (github.com/oostendo/python-zxing)
    '''