# Copyright (2016) Alok Parlikar <alok@parlikar.com>

import pyflite
import os
import sys

if not os.path.exists("cmu_us_rms.flitevox"):
    print("You need to download a voice to test this.  See the README")
    sys.exit(1)

pyflite.init()

x = pyflite.select_voice("cmu_us_rms.flitevox")
y = pyflite.text_to_wave("A whole joy was reaping, but they've gone south.", x)

samples = y["samples"]
sample_rate = y["sample_rate"]

import wave
import struct

nchannels = 1
sampwidth = 2
samplingrate = int(sample_rate)
nframes   = len(samples)
comptype  = "NONE"
compname = "not compressed"

wav_file = wave.open("sample.wav", "w")

wav_file.setparams((1, sampwidth, samplingrate, nframes,
comptype, compname))


for s in samples:
    # write the audio frames to file
    wav_file.writeframes(struct.pack('h', int(s)))
    # print int(s*amp/2)
wav_file.close()