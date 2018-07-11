# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class OcrResult(Model):
    """OcrResult.

    :param language: The BCP-47 language code of the text in the image.
    :type language: str
    :param text_angle: The angle, in degrees, of the detected text with
     respect to the closest horizontal or vertical direction. After rotating
     the input image clockwise by this angle, the recognized text lines become
     horizontal or vertical. In combination with the orientation property it
     can be used to overlay recognition results correctly on the original
     image, by rotating either the original image or recognition results by a
     suitable angle around the center of the original image. If the angle
     cannot be confidently detected, this property is not present. If the image
     contains text at different angles, only part of the text will be
     recognized correctly.
    :type text_angle: float
    :param orientation: Orientation of the text recognized in the image. The
     value (up,down,left, or right) refers to the direction that the top of the
     recognized text is facing, after the image has been rotated around its
     center according to the detected text angle (see textAngle property).
    :type orientation: str
    :param regions: An array of objects, where each object represents a region
     of recognized text.
    :type regions:
     list[~azure.cognitiveservices.vision.computervision.models.OcrRegion]
    """

    _attribute_map = {
        'language': {'key': 'language', 'type': 'str'},
        'text_angle': {'key': 'textAngle', 'type': 'float'},
        'orientation': {'key': 'orientation', 'type': 'str'},
        'regions': {'key': 'regions', 'type': '[OcrRegion]'},
    }

    def __init__(self, **kwargs):
        super(OcrResult, self).__init__(**kwargs)
        self.language = kwargs.get('language', None)
        self.text_angle = kwargs.get('text_angle', None)
        self.orientation = kwargs.get('orientation', None)
        self.regions = kwargs.get('regions', None)
