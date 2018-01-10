from __future__ import print_function
import os
import Image
import StringIO
import io


def setup(classpath, java_home):
    os.environ['JAVA_HOME'] = java_home
    import jnius_config
    jnius_config.add_classpath(classpath)


# runner = autoclass('com.google.zxing.client.j2se.CommandLineRunnerCustom')
# runner.readFromFileSystem(['goal_qrcode.png'])


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
    CommandLineRunner = autoclass('com.google.zxing.client.j2se.CommandLineRunnerCustom')
    # BufferedImageLuminanceSource = autoclass('com.google.zxing.BufferedImageLuminanceSource')
    LuminanceSource = autoclass('com.google.zxing.LuminanceSource')
    # HybridBinarizer = autoclass('com.google.zxing.HybridBinarizer')
    Binarizer = autoclass('com.google.zxing.Binarizer')
    BinaryBitmap = autoclass('com.google.zxing.BinaryBitmap')
    QRCodeReader = autoclass('com.google.zxing.qrcode.QRCodeReader')
    MultiFormatReader = autoclass('com.google.zxing.MultiFormatReader')

    byteArray = ByteBuffer.wrap(serialized_img)
    imageByteArray = byteArray.array()
    byteInputStream = ByteArrayInputStream(imageByteArray)

    imageInputStream = ImageIO.createImageInputStream(byteInputStream)
    bufferedImage = ImageIO.read(imageInputStream)

    source = LuminanceSource(bufferedImage)
    bitmap = BinaryBitmap(Binarizer(source))
    reader = MultiFormatReader()

    result = reader.decode(bitmap)
    text = result.getText()
    return text





