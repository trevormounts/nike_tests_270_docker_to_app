import logging
import time
import os

log = logging.getLogger(__name__)

MAX_SWIPES = 10


def run(context):
    button_demo = False
    attempts = 0

    button_demo = element_exists(context, 'div_neutrals_by_you')
    
    while not button_demo and attempts <= MAX_SWIPES:
        attempts += 1
        context.perform_gesture('swipe_up', '')
        button_demo = element_exists(context, 'div_neutrals_by_you')

    context.verify(['div_neutrals_by_you'])


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0
