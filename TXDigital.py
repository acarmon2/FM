#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Txdigital
# Generated: Mon Jul 25 19:25:30 2016
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import time
import wx

class TXDigital(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Txdigital")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.baud_rate = baud_rate = 49260
        self.samp_rate = samp_rate = baud_rate*10
        self.deviation = deviation = 180000
        self.sps = sps = samp_rate/baud_rate
        self.samp_rate_TX = samp_rate_TX = samp_rate*2
        self.modulation_index = modulation_index = (float)(deviation)/((float)(baud_rate / 2))

        ##################################################
        # Blocks
        ##################################################
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	device_addr="",
        	stream_args=uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate_TX)
        self.uhd_usrp_sink_0.set_center_freq(434e6, 0)
        self.uhd_usrp_sink_0.set_gain(20, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.rational_resampler_xxx_0 = filter.rational_resampler_ccc(
                interpolation=samp_rate_TX,
                decimation=samp_rate,
                taps=None,
                fractional_bw=None,
        )
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.8, ))
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/gema/Documents/RF12B.dat", True)
        self.analog_cpfsk_bc_0 = analog.cpfsk_bc((float)((float)(deviation)/baud_rate), 0.1, sps)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.analog_cpfsk_bc_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.analog_cpfsk_bc_0, 0))


# QT sink close method reimplementation

    def get_baud_rate(self):
        return self.baud_rate

    def set_baud_rate(self, baud_rate):
        self.baud_rate = baud_rate
        self.set_samp_rate(self.baud_rate*10)
        self.set_modulation_index((float)(self.deviation)/((float)(self.baud_rate / 2)))
        self.set_sps(self.samp_rate/self.baud_rate)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.set_sps(self.samp_rate/self.baud_rate)
        self.set_samp_rate_TX(self.samp_rate*2)

    def get_deviation(self):
        return self.deviation

    def set_deviation(self, deviation):
        self.deviation = deviation
        self.set_modulation_index((float)(self.deviation)/((float)(self.baud_rate / 2)))

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate_TX(self):
        return self.samp_rate_TX

    def set_samp_rate_TX(self, samp_rate_TX):
        self.samp_rate_TX = samp_rate_TX
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate_TX)

    def get_modulation_index(self):
        return self.modulation_index

    def set_modulation_index(self, modulation_index):
        self.modulation_index = modulation_index

if __name__ == '__main__':
    import ctypes
    import os
    if os.name == 'posix':
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    (options, args) = parser.parse_args()
    tb = TXDigital()
    tb.Start(True)
    tb.Wait()

