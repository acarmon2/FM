#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Mon Jul 25 18:33:45 2016
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import math
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 1000000
        self.deviation = deviation = 180000
        self.baud_rate = baud_rate = 49260
        self.sps = sps = ((float)(samp_rate)/(float)(baud_rate))
        self.modulation_index = modulation_index = (float)(deviation) / ((float)(baud_rate) / 2)
        self.Threshold = Threshold = -60
        self.Freq = Freq = 434000000

        ##################################################
        # Blocks
        ##################################################
        _Freq_sizer = wx.BoxSizer(wx.VERTICAL)
        self._Freq_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_Freq_sizer,
        	value=self.Freq,
        	callback=self.set_Freq,
        	label="Frequency",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._Freq_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_Freq_sizer,
        	value=self.Freq,
        	callback=self.set_Freq,
        	minimum=430000000,
        	maximum=440000000,
        	num_steps=1000,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_Freq_sizer)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(Freq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_bandwidth(samp_rate, 0)
        self.low_pass_filter_0_0 = filter.fir_filter_fff(1, firdes.low_pass(
        	1, samp_rate, 100e3, 100e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0 = filter.fir_filter_ccf(1, firdes.low_pass(
        	1, samp_rate, 200e3, 100e3, firdes.WIN_HAMMING, 6.76))
        self.digital_clock_recovery_mm_xx_0 = digital.clock_recovery_mm_ff(sps*(1+0.0), 0.1, 0, 0.1, 0.01)
        self.digital_binary_slicer_fb_0 = digital.binary_slicer_fb()
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/augusto/Documents/RXDigital.dat", False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.analog_quadrature_demod_cf_0 = analog.quadrature_demod_cf((float)(sps)/(math.pi * modulation_index))
        self.analog_pwr_squelch_xx_0 = analog.pwr_squelch_cc(Threshold, 1, 0, False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pwr_squelch_xx_0, 0), (self.low_pass_filter_0, 0))    
        self.connect((self.analog_quadrature_demod_cf_0, 0), (self.low_pass_filter_0_0, 0))    
        self.connect((self.digital_binary_slicer_fb_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.digital_clock_recovery_mm_xx_0, 0), (self.digital_binary_slicer_fb_0, 0))    
        self.connect((self.low_pass_filter_0, 0), (self.analog_quadrature_demod_cf_0, 0))    
        self.connect((self.low_pass_filter_0_0, 0), (self.digital_clock_recovery_mm_xx_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.analog_pwr_squelch_xx_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(((float)(self.samp_rate)/(float)(self.baud_rate)))
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_bandwidth(self.samp_rate, 0)
        self.low_pass_filter_0_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 100e3, firdes.WIN_HAMMING, 6.76))
        self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 200e3, 100e3, firdes.WIN_HAMMING, 6.76))

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation
        self.set_modulation_index((float)(self.deviation) / ((float)(self.baud_rate) / 2))

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_sps(((float)(self.samp_rate)/(float)(self.baud_rate)))
        self.set_modulation_index((float)(self.deviation) / ((float)(self.baud_rate) / 2))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_clock_recovery_mm_xx_0.set_omega(self.sps*(1+0.0))
        self.analog_quadrature_demod_cf_0.set_gain((float)(self.sps)/(math.pi * self.modulation_index))

    def get_modulation_index(self):
        return self.modulation_index

    def set_modulation_index(self, modulation_index):
        self.modulation_index = modulation_index
        self.analog_quadrature_demod_cf_0.set_gain((float)(self.sps)/(math.pi * self.modulation_index))

    def get_Threshold(self):
        return self.Threshold

    def set_Threshold(self, Threshold):
        self.Threshold = Threshold
        self.analog_pwr_squelch_xx_0.set_threshold(self.Threshold)

    def get_Freq(self):
        return self.Freq

    def set_Freq(self, Freq):
        self.Freq = Freq
        self._Freq_slider.set_value(self.Freq)
        self._Freq_text_box.set_value(self.Freq)
        self.uhd_usrp_source_0.set_center_freq(self.Freq, 0)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
