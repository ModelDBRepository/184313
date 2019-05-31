'''
Defines a class, Neuron473465456, of neurons from Allen Brain Institute's model 473465456

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473465456:
    def __init__(self, name="Neuron473465456", x=0, y=0, z=0):
        '''Instantiate Neuron473465456.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473465456_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg2-Cre_Ai14_IVSCC_-167081.03.02.01_397905347_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473465456_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 277.21
            sec.e_pas = -75.5092086792
        for sec in self.apic:
            sec.cm = 3.56
            sec.g_pas = 0.000559550096981
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.00028096175735
        for sec in self.dend:
            sec.cm = 3.56
            sec.g_pas = 0.000682496872246
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.0052482
            sec.gbar_Ih = 0.0129501
            sec.gbar_NaTs = 0.265873
            sec.gbar_Nap = 0.00133651
            sec.gbar_K_P = 0.00842096
            sec.gbar_K_T = 0.000443676
            sec.gbar_SK = 0.000325567
            sec.gbar_Kv3_1 = 0.00707627
            sec.gbar_Ca_HVA = 0.000323393
            sec.gbar_Ca_LVA = 0.00233324
            sec.gamma_CaDynamics = 0.00169369
            sec.decay_CaDynamics = 903.772
            sec.g_pas = 0.000882564
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

