import os        as _os
import numpy     as _n
import spinmob   as _s
import mcphysics as _m
import unittest  as _ut
import shutil    as _sh

# Globals for monkeywork on the command line
a = b = c = d = x = None

if _os.path.exists('egg_settings'): _sh.rmtree('egg_settings')

# Path to the data folder
data_path = _os.path.join(_os.path.dirname(_m.__file__), '_tests', 'data')
def path(filename):
    """
    Assembles a path to a particular file.
    """
    return _os.path.join(data_path, filename)


class Test_errthing(_ut.TestCase):
    """
    Test class for mcphysics library.
    """


    def setUp(self):
        return
    
    def tearDown(self):
        return

    def test_data(self):
        
        d = _m.data.load_chn(path('signal.Chn'))
        self.assertEqual(len(d), 2)
        self.assertEqual(len(d[1]), 1024)

        ds = _m.data.load_chns([path('signal.Chn'), path('background.Chn')])
        self.assertEqual(len(ds), 2)
        self.assertEqual(len(ds[1]), 2)
    
        _m.data.plot_chn_files(paths=[path('signal.Chn'), path('background.Chn')])
    
        image = _m.data.load_image(path('image.jpg'))
        self.assertEqual(image.shape, (612, 816, 3))
        
        images = _m.data.load_images([path('image.jpg')])
        self.assertEqual(_n.shape(images), (1,612,816,3))
    
    
    def test_functions(self):
        
        _s.plot.xy.function(['em_gaussian(x,1,2)', 'voigt(x,2,1)', 'erfcx(x)', 'reduced_chi2(x,10)'], 
                             1e-6,5,1000,g=_m.functions.__dict__)
    
    def test_instruments(self):
        global a, c
        
        a = _m.instruments.sillyscope(block=True)
        c = _m.instruments.keithley_dmm(block=True)
    
    def test_playground(self):
        global b
        
        b = _m.playground.fitting_statistics_demo(block=True)
        
        print()
        _m.playground.plot_and_integrate_reduced_chi2()
    
if __name__ == "__main__":
    _ut.main()
