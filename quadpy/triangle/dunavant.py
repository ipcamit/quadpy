# -*- coding: utf-8 -*-
#
from sympy import Rational

from .helpers import _s3, _s21, _s111 as fs

from ..helpers import untangle


class Dunavant(object):
    '''
    Triangle integration schemes from

    D. A. Dunavant,
    High Degree Efficient Symmetrical Gaussian Quadrature Rules for the
    Triangle,
    Article in International Journal for Numerical Methods in Engineering,
    21(6):1129-1148, June 1985,
    10.1002/nme.1620210612,
    <https://dx.doi.org/10.1002/nme.1620210612>.
    '''
    def __init__(self, index):
        self.name = 'Dunavant(%d)' % index
        if index == 1:
            self.degree = 1
            data = [(1, _s3())]
        elif index == 2:
            self.degree = 2
            data = [(Rational(1, 3), _s21(Rational(1, 6)))]
        elif index == 3:
            self.degree = 3
            data = [
                (-Rational(9, 16), _s3()),
                (Rational(25, 48), _s21(Rational(1, 5))),
                ]
        elif index == 4:
            self.degree = 4
            data = [
                (0.223381589678011, _s21(0.445948490915965)),
                (0.109951743655322, _s21(0.091576213509771)),
                ]
        elif index == 5:
            self.degree = 5
            data = [
                (0.225, _s3()),
                (0.132394152788506, _s21(0.4701420641051)),
                (0.125939180544827, _s21(0.101286507323456)),
                ]
        elif index == 6:
            self.degree = 6
            data = [
                (0.116786275726379, _s21(0.249286745170910)),
                (0.050844906370207, _s21(0.063089014491502)),
                (0.082851075618374, fs(0.053145049844817, 0.310352451033784)),
                ]
        elif index == 7:
            self.degree = 7
            data = [
                (-0.149570044467682, _s3()),
                (+0.175615257433208, _s21(0.260345966079040)),
                (+0.053347235608838, _s21(0.065130102902216)),
                (+0.077113760890257, fs(0.048690315425316, 0.312865496004874)),
                ]
        elif index == 8:
            self.degree = 8
            data = [
                (0.144315607677787, _s3()),
                (0.095091634267285, _s21(0.459292588292723)),
                (0.103217370534718, _s21(0.170569307751760)),
                (0.032458497623198, _s21(0.050547228317031)),
                (0.027230314174435, fs(0.008394777409958, 0.263112829634638)),
                ]
        elif index == 9:
            self.degree = 9
            data = [
                (0.097135796282799, _s3()),
                (0.031334700227139, _s21(0.489682519198738)),
                (0.077827541004774, _s21(0.437089591492937)),
                (0.079647738927210, _s21(0.188203535619033)),
                (0.025577675658698, _s21(0.044729513394453)),
                (0.043283539377289, fs(0.036838412054736, 0.221962989160766)),
                ]
        elif index == 10:
            self.degree = 10
            data = [
                (0.090817990382754, _s3()),
                (0.036725957756467, _s21(0.485577633383657)),
                (0.045321059435528, _s21(0.109481575485037)),
                (0.072757916845420, fs(0.141707219414880, 0.307939838764121)),
                (0.028327242531057, fs(0.025003534762686, 0.246672560639903)),
                (0.009421666963733, fs(0.009540815400299, 0.066803251012200)),
                ]
        elif index == 11:
            self.degree = 11
            data = [
                (0.000927006328961, _s21(0.534611048270758)),
                (0.077149534914813, _s21(0.398969302965855)),
                (0.059322977380774, _s21(0.203309900431282)),
                (0.036184540503418, _s21(0.119350912282581)),
                (0.013659731002678, _s21(0.032364948111276)),
                (0.052337111962204, fs(0.050178138310495, 0.356620648261293)),
                (0.020707659639141, fs(0.021022016536166, 0.171488980304042)),
                ]
        elif index == 12:
            self.degree = 12
            data = [
                (0.025731066440455, _s21(0.488217389773805)),
                (0.043692544538038, _s21(0.439724392294460)),
                (0.062858224217885, _s21(0.271210385012116)),
                (0.034796112930709, _s21(0.127576145541586)),
                (0.006166261051559, _s21(0.021317350453210)),
                (0.040371557766381, fs(0.115343494534698, 0.275713269685514)),
                (0.022356773202303, fs(0.022838332222257, 0.281325580989940)),
                (0.017316231108659, fs(0.025734050548330, 0.116251915907597)),
                ]
        elif index == 13:
            self.degree = 13
            data = [
                (0.052520923400802, _s3()),
                (0.011280145209330, _s21(0.495048184939705)),
                (0.031423518362454, _s21(0.468716635109574)),
                (0.047072502504194, _s21(0.414521336801277)),
                (0.047363586536355, _s21(0.229399572042831)),
                (0.031167529045794, _s21(0.114424495196330)),
                (0.007975771465074, _s21(0.024811391363459)),
                (0.036848402728732, fs(0.094853828379579, 0.268794997058761)),
                (0.017401463303822, fs(0.018100773278807, 0.291730066734288)),
                (0.015521786839045, fs(0.022233076674090, 0.126357385491669)),
                ]
        elif index == 14:
            self.degree = 14
            data = [
                (0.021883581369429, _s21(0.488963910362179)),
                (0.032788353544125, _s21(0.417644719340454)),
                (0.051774104507292, _s21(0.273477528308839)),
                (0.042162588736993, _s21(0.177205532412543)),
                (0.014433699669777, _s21(0.061799883090873)),
                (0.004923403602400, _s21(0.019390961248701)),
                (0.024665753212564, fs(0.057124757403648, 0.172266687821356)),
                (0.038571510787061, fs(0.092916249356972, 0.336861459796345)),
                (0.014436308113534, fs(0.014646950055654, 0.298372882136258)),
                (0.005010228838501, fs(0.001268330932872, 0.118974497696957)),
                ]
        elif index == 15:
            self.degree = 15
            data = [
                (0.001916875642849, _s21(0.506972916858243)),
                (0.044249027271145, _s21(0.431406354283023)),
                (0.051186548718852, _s21(0.277693644847144)),
                (0.023687735870688, _s21(0.126464891041254)),
                (0.013289775690021, _s21(0.070808385974686)),
                (0.004748916608192, _s21(0.018965170241073)),
                (0.038550072599593, fs(+0.133734161966621, 0.261311371140087)),
                (0.027215814320624, fs(+0.036366677396917, 0.575586555512814)),
                (0.002182077366797, fs(-0.010174883126571, 0.285712220049916)),
                (0.021505319847731, fs(+0.036843869875878, 0.215599664072284)),
                (0.007673942631049, fs(+0.012459809331199, 0.103575616576386)),
                ]
        elif index == 16:
            self.degree = 16
            data = [
                (0.046875697427642, _s3()),
                (0.006405878578585, _s21(0.497380541948438)),
                (0.041710296739387, _s21(0.413469438549352)),
                (0.026891484250064, _s21(0.470458599066991)),
                (0.042132522761650, _s21(0.240553749969521)),
                (0.030000266842773, _s21(0.147965794222573)),
                (0.014200098925024, _s21(0.075465187657474)),
                (0.003582462351273, _s21(0.016596402623025)),
                (0.032773147460627, fs(+0.103575692245252, 0.296555596579887)),
                (0.015298306248441, fs(+0.020083411655416, 0.337723063403079)),
                (0.002386244192839, fs(-0.004341002614139, 0.204748281642812)),
                (0.019084792755899, fs(+0.041941786468010, 0.189358492130623)),
                (0.006850054546542, fs(+0.014317320230681, 0.085283615682657)),
                ]
        elif index == 17:
            self.degree = 17
            data = [
                (0.033437199290803, _s3()),
                (0.005093415440507, _s21(0.497170540556774)),
                (0.014670864527638, _s21(0.482176322624625)),
                (0.024350878353672, _s21(0.450239969020782)),
                (0.031107550868969, _s21(0.400266239377397)),
                (0.031257111218620, _s21(0.252141267970953)),
                (0.024815654339665, _s21(0.162047004658461)),
                (0.014056073070557, _s21(0.075875882260746)),
                (0.003194676173779, _s21(0.015654726967822)),
                (0.008119655318993, fs(0.334319867363658, 0.655493203809423)),
                (0.026805742283163, fs(0.292221537796944, 0.572337590532020)),
                (0.018459993210822, fs(0.319574885423190, 0.626001190286228)),
                (0.008476868534328, fs(0.190704224192292, 0.796427214974071)),
                (0.018292796770025, fs(0.180483211648746, 0.752351005937729)),
                (0.006665632004165, fs(0.080711313679564, 0.904625504095608)),
                ]
        elif index == 18:
            self.degree = 18
            data = [
                (+0.030809939937647, _s3()),
                (+0.009072436679404, _s21(0.493344808630921)),
                (+0.018761316939594, _s21(0.469210594241957)),
                (+0.019441097985477, _s21(0.436281395887006)),
                (+0.027753948610810, _s21(0.394846170673416)),
                (+0.032256225351457, _s21(0.249794568803157)),
                (+0.025074032616922, _s21(0.161432193743843)),
                (+0.015271927971832, _s21(0.076598227485371)),
                (+0.006793922022963, _s21(0.024252439353450)),
                (-0.002223098729920, _s21(0.043146367216965)),
                (+0.006331914076406, fs(0.358911494940944, 0.632657968856636)),
                (+0.027257538049138, fs(0.294402476751957, 0.574410971510855)),
                (+0.017676785649465, fs(0.325017801641814, 0.624779046792512)),
                (+0.018379484638070, fs(0.184737559666046, 0.748933176523037)),
                (+0.008104732808192, fs(0.218796800013321, 0.769207005420443)),
                (+0.007634129070725, fs(0.101179597136408, 0.883962302273467)),
                (+0.000046187660794, fs(0.020874755282586, 1.014347260005363)),
                ]
        elif index == 19:
            self.degree = 19
            data = [
                (0.032906331388919, _s3()),
                (0.010330731891272, _s21(0.489609987073006)),
                (0.022387247263016, _s21(0.454536892697893)),
                (0.030266125869468, _s21(0.401416680649431)),
                (0.030490967802198, _s21(0.255551654403098)),
                (0.024159212741641, _s21(0.177077942152130)),
                (0.016050803586801, _s21(0.110061053227952)),
                (0.008084580261784, _s21(0.055528624251840)),
                (0.002079362027485, _s21(0.012621863777229)),
                (0.003884876904981, fs(0.395754787356943, 0.600633794794645)),
                (0.025574160612022, fs(0.307929983880436, 0.557603261588784)),
                (0.008880903573338, fs(0.264566948406520, 0.720987025817365)),
                (0.016124546761731, fs(0.358539352205951, 0.594527068955871)),
                (0.002491941817491, fs(0.157807405968595, 0.839331473680839)),
                (0.018242840118951, fs(0.075050596975911, 0.701087978926173)),
                (0.010258563736199, fs(0.142421601113383, 0.822931324069857)),
                (0.003799928855302, fs(0.065494628082938, 0.924344252620784)),
                ]
        else:
            assert index == 20
            self.degree = 20
            data = [
                (+0.033057055541624, _s3()),
                (+0.000867019185663, _s21(0.500950464352200)),
                (+0.011660052716448, _s21(0.488212957934729)),
                (+0.022876936356421, _s21(0.455136681950283)),
                (+0.030448982673938, _s21(0.401996259318289)),
                (+0.030624891725355, _s21(0.255892909759421)),
                (+0.024368057676800, _s21(0.176488255995106)),
                (+0.015997432032024, _s21(0.104170855336758)),
                (+0.007698301815602, _s21(0.053068963840930)),
                (-0.000632060497488, _s21(0.041618715196029)),
                (+0.001751134301193, _s21(0.011581921406822)),
                (+0.016465839189576, fs(0.344855770229001, 0.606402646106160)),
                (+0.004839033540485, fs(0.377843269594854, 0.615842614456541)),
                (+0.025804906534650, fs(0.306635479062357, 0.559048000390295)),
                (+0.008471091054441, fs(0.249419362774742, 0.736606743262866)),
                (+0.018354914106280, fs(0.212775724802802, 0.711675142287434)),
                (+0.000704404677908, fs(0.146965436053239, 0.861402717154987)),
                (+0.010112684927462, fs(0.137726978828923, 0.835586957912363)),
                (+0.003573909385950, fs(0.059696109149007, 0.929756171556853)),
                ]

        # convert self.barycentric coordinates to reference triangle
        self.bary, self.weights = untangle(data)
        self.points = self.bary[:, 1:]
        return
