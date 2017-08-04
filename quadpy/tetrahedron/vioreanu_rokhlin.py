# -*- coding: utf-8 -*-
#
from .helpers import _s4, _s31, _s22, _s211, _s1111

from ..helpers import untangle


class VioreanuRokhlin(object):
    '''
    B. Vioreanu and V. Rokhlin,
    Spectra of Multiplication Operators as a Numerical Tool,
    Methods and Algorithms for Scientific Computing,
    2014,
    SIAM J. Sci. Comput., 36(1), A267–A288,
    <https://doi.org/10.1137/110860082>,
    <http://www.cs.yale.edu/publications/techreports/tr1443.pdf>.

    Data adapted from modepy
    <https://github.com/inducer/modepy/blob/master/modepy/quadrature/vr_quad_data_tet.py>.
    '''
    def __init__(self, index):
        self.name = 'VioreanuRokhlin({})'.format(index)
        if index == 0:
            self.degree = 1
            data = [
                (4.0/3.0, _s4()),
                ]
        elif index == 1:
            self.degree = 2
            data = [
                (1.0/3.0, _s31(1.381966011250106e-01)),
                ]
        elif index == 2:
            self.degree = 3
            data = [
                (6.722501662827225e-02, _s31(7.714091970968884e-02)),
                (1.774055444700407e-01, _s22(4.059745208742446e-01)),
                ]
        elif index == 3:
            self.degree = 5
            data = [
                (3.647345460966428e-02, _s31(6.994279207826770e-02)),
                (5.443787015468327e-02, _s211(6.164442753123828e-02, 5.838467212163365e-01)),
                (1.335462682596192e-01, _s31(3.097442551731893e-01)),
                ]
        elif index == 4:
            self.degree = 6
            data = [
                (1.115617800911627e-02, _s31(4.481876259019502e-02)),
                (2.149874196554802e-02, _s211(4.431548387057316e-02, 7.009568921763990e-01)),
                (2.932785970523123e-02, _s22(4.535094091980409e-01)),
                (6.108234662137460e-02, _s211(2.272082578263463e-01, 5.104553962651259e-02)),
                (1.217684000224085e-01, _s4()),
                ]
        elif index == 5:
            self.degree = 7
            data = [
                (8.393257975516334e-03, _s211(3.403237404201720e-02, 7.679769895445143e-01)),
                (9.851051861183095e-03, _s31(4.717778359328573e-02)),
                (1.823867305835592e-02, _s211(4.026038652328617e-02, 5.785386005230662e-01)),
                (2.884515620851804e-02, _s211(1.847132125389332e-01, 3.986787209774240e-02)),
                (3.063482006319787e-02, _s211(3.851844624255586e-01, 1.892713069674117e-01)),
                (6.514655955538516e-02, _s31(1.953741548049375e-01)),
                ]
        elif index == 6:
            self.degree = 9
            data = [
                (4.285129606204518e-03, _s211(2.746372670954444e-02, 8.069307625165607e-01)),
                (4.945914135463306e-03, _s31(3.556631480914729e-02)),
                (7.439006613987653e-03, _s211(2.958339293908863e-02, 6.778165664396495e-01)),
                (9.250687037503105e-03, _s22(2.788965124806808e-02)),
                (1.453642863447186e-02, _s211(1.464088963597444e-01, 3.036385732664770e-02)),
                (1.762601881781520e-02, _s1111(5.071064293713055e-01, 3.193022325264996e-01, 1.429601001927085e-01)),
                (2.522896190677588e-02, _s31(3.226117863678400e-01)),
                (3.402441161166769e-02, _s31(1.512007882172118e-01)),
                (4.714680510152520e-02, _s22(3.437976739841325e-01)),
                ]
        elif index == 7:
            self.degree = 10
            data = [
                (1.262683197423406e-03, _s31(1.941122489301828e-02)),
                (3.816360181044174e-03, _s211(2.703350840562557e-02, 7.293926850123016e-01)),
                (3.858627669230225e-03, _s211(2.648226491257816e-02, 8.346860742795041e-01)),
                (5.401271899284645e-03, _s211(2.233333002918325e-02, 5.855325724314953e-01)),
                (6.749263744790283e-03, _s211(1.204991798045645e-01, 2.218610635475460e-02)),
                (1.078862373479965e-02, _s211(4.304204597375166e-01, 1.136247661434978e-01)),
                (1.171751035102570e-02, _s1111(5.808224332151291e-01, 2.655436309321665e-01, 1.265978171994966e-01)),
                (1.326836978850226e-02, _s211(2.743983921192598e-01, 2.644624205083912e-02)),
                (2.170104502184572e-02, _s31(1.255838222754385e-01)),
                (2.545990060255948e-02, _s211(1.317016306156411e-01, 4.510721858498442e-01)),
                (3.203729014727367e-02, _s31(2.892110643292711e-01)),
                ]
        elif index == 8:
            self.degree = 11
            data = [
                (9.695447888568765e-04, _s211(2.388787886656957e-02, 8.705443116154074e-01)),
                (1.959903828226847e-03, _s31(2.617103277295219e-02)),
                (2.292744495731360e-03, _s22(1.375236581886419e-02)),
                (2.802692325922526e-03, _s211(1.903349443211699e-02, 7.970471485218408e-01)),
                (3.118388063437694e-03, _s211(1.008596673993710e-01, 1.436337595093029e-02)),
                (4.365256048613347e-03, _s211(2.434906451212993e-02, 6.322506459263664e-01)),
                (5.950359199919208e-03, _s1111(6.716079793211197e-01, 2.028653638555222e-01, 1.012015873047946e-01)),
                (8.415560627784396e-03, _s1111(5.181755993267751e-01, 3.567323365469498e-01, 1.028384582772451e-01)),
                (8.645355473711726e-03, _s211(3.718666283348195e-01, 2.352758046590782e-01)),
                (9.480997640758474e-03, _s211(2.247178848749781e-01, 2.248198827546399e-02)),
                (1.324205607746111e-02, _s31(1.006862685057424e-01)),
                (1.508897928856845e-02, _s22(3.881547512699796e-01)),
                (1.806093108194538e-02, _s211(1.171336251346634e-01, 5.212126864871611e-01)),
                (1.842574822070229e-02, _s211(2.516437633635237e-01, 1.073345337250223e-01)),
                (3.302611141250949e-02, _s4()),
                ]
        else:
            assert index == 9
            self.degree = 13
            data = [
                (5.973324616573234e-04, _s211(1.330521685089425e-02, 9.020031738386604e-01)),
                (9.867179979395793e-04, _s31(2.195048789714021e-02)),
                (1.530602010365591e-03, _s211(1.768399597717130e-02, 8.196215282360872e-01)),
                (1.747170153157562e-03, _s211(1.529671184250192e-02, 7.011322545807197e-01)),
                (2.084303013925438e-03, _s211(1.653903692788761e-02, 5.552429363123564e-01)),
                (2.673796478110494e-03, _s211(8.507539000069664e-02, 1.623321259293437e-02)),
                (3.095950883546983e-03, _s1111(7.235027978629237e-01, 1.786655410279764e-01, 7.971539172604925e-02)),
                (5.138056712393536e-03, _s1111(5.990133535361137e-01, 2.979840982969011e-01, 8.413051172360086e-02)),
                (5.506829153098441e-03, _s31(3.276176808608863e-01)),
                (5.719278052186033e-03, _s211(4.469402940184373e-01, 8.675844882562167e-02)),
                (6.394220575258051e-03, _s211(1.891121490910459e-01, 1.892485052021575e-02)),
                (6.405474784136410e-03, _s1111(4.568679514095241e-01, 3.253255095768594e-01, 1.994214547588828e-01)),
                (6.875685401153072e-03, _s31(8.433252216723813e-02)),
                (1.066709630566213e-02, _s211(9.719941787513314e-02, 4.601344642402377e-01)),
                (1.229281709786569e-02, _s211(3.463288089439753e-01, 2.155054870671660e-01)),
                (1.250759519378543e-02, _s211(9.576008835067273e-02, 6.023289518800232e-01)),
                (1.404082813990796e-02, _s211(2.204649331210681e-01, 9.329765691467751e-02)),
                (2.136208805503387e-02, _s31(2.136603304379895e-01)),
                ]

        self.bary, self.weights = untangle(data)
        self.points = self.bary[:, 1:]
        self.weights *= 3.0 / 4.0
        return
