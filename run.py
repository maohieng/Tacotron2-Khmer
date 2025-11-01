import re
from text2num.text.num2word import num2word, num_en2km
from khmernltk import word_tokenize
import matplotlib.pylab as plt
import torch
import numpy as np
import torch
from model import Tacotron2
from text import text_to_sequence


def text_process(text):
    text = word_tokenize(text)
    text = " ".join(word for word in text)
#     final += " ."
    return text

def textNorm(text):
    text = re.sub(r"[0-9]+", num_en2km, text)
    text = re.sub(r"[+-]?([០-៩]*[,])?[០-៩]+", num2word, text)
    curlist = {
        "$": "ដុល្លារ",
        "៛": "រៀល",
        "€": "អឺរ៉ូ",
        "¥": "យេន",
        "￥": "យន់",
        "₹": "រូពី",
        "£": "ផោន",
        "฿": "បាត",
        "₫": "ដុង",
        "₭": "គីប",
    }
    punctuation = r"!?,.;។"
    if (text[-1] != punctuation) : text = text + ';'
    text = re.sub(r"[$៛€¥￥₹£฿₫₭]", lambda m: curlist.get(m.group()), text)
    print(text)
    return text

def plot_data(data, figsize=(16, 4)):
    fig, axes = plt.subplots(1, len(data), figsize=figsize)
    for i in range(len(data)):
        axes[i].imshow(data[i], aspect='auto', origin='bottom', 
                       interpolation='none')
        
