from matplotlib import pyplot as plt
import numpy as np
import operator

num_epochs=100

def LearningLoss():

    trial_mean_acc_features={}
    trial_mean_acc_features_feature3 = {}
    trial_mean_acc_features_feature2 = {}
    trial_mean_acc_features_feature1 = {}
    trial_mean_time_features={}
    trial_mean_time_features_feature3 = {}
    trial_mean_time_features_feature2 = {}
    trial_mean_time_features_feature1 = {}


    fig = plt.figure(figsize=(20, 40))
    x = np.linspace(1, 10, 10)

    #Test accuracy

    trial1_acc_feature0123 = [49.03, 63.56, 71.17, 79.74, 82.67, 86.2, 87.53, 88.96, 90.04, 90.11]
    trial2_acc_feature0123 = [46.31, 59.02, 69.58, 79.14, 82.78, 86.33, 87.37, 88.71, 89.57, 90.11]
    trial3_acc_feature0123 = [45.31, 60.23, 72.01, 80.04, 82.96, 86.57, 87.75, 89.26, 89.73, 90.58]
    trial_mean_acc_feature0123 = [(trial1_acc_feature0123[i]+trial2_acc_feature0123[i]+trial3_acc_feature0123[i])/3 for i in range(0,10)]
    trial_mean_acc_features['f 1,2,3,4'] = trial_mean_acc_feature0123
    trial_mean_acc_features_feature3['f 1,2,3,4']= trial_mean_acc_feature0123
    trial_mean_acc_features_feature2['f 1,2,3,4']=trial_mean_acc_feature0123
    trial_mean_acc_features_feature1['f 1,2,3,4']=trial_mean_acc_feature0123

    trial1_acc_feature012 = [43.88, 54.84, 63.29, 72.31, 79.8, 84.34, 85.79, 86.9, 88.07, 88.43]
    trial2_acc_feature012 = [46.96, 55.73, 64.1, 71.16, 77.75, 81.89, 84.73, 86.05, 87.32, 87.87]
    trial3_acc_feature012 = [45.91, 53.31, 62.83, 72.14, 79.0, 83.39, 85.39, 86.44, 87.46, 88.32]
    trial_mean_acc_feature012 = [
        (trial1_acc_feature012[i] + trial2_acc_feature012[i] + trial3_acc_feature012[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1,2,3'] = trial_mean_acc_feature012
    trial_mean_acc_features_feature3['f 1,2,3'] = trial_mean_acc_feature012

    trial1_acc_feature013 = [48.64, 61.03, 71.48, 80.39, 83.34, 86.33, 87.73, 88.98, 89.6, 90.2]
    trial2_acc_feature013 = [49.64, 64.93, 73.63, 80.99, 83.77, 86.13, 87.72, 89.04, 89.05, 90.02]
    trial3_acc_feature013 = [46.95, 57.05, 67.03, 76.9, 82.16, 85.07, 87.02, 88.11, 89.12, 89.55]
    trial_mean_acc_feature013 = [
        (trial1_acc_feature013[i] + trial2_acc_feature013[i] + trial3_acc_feature013[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1,2,4'] = trial_mean_acc_feature013
    trial_mean_acc_features_feature3['f 1,2,4'] = trial_mean_acc_feature013

    trial1_acc_feature023 = [47.98, 63.22, 72.84, 80.98, 83.62, 86.32, 87.85, 89.03, 89.5, 90.48]
    trial2_acc_feature023 = [47.12, 60.07, 70.81, 80.05, 83.71, 86.03, 87.41, 88.4, 89.18, 90.43]
    trial3_acc_feature023 = [45.62, 58.18, 69.33, 79.02, 82.57, 85.53, 87.06, 88.36, 89.54, 89.65]
    trial_mean_acc_feature023 = [
        (trial1_acc_feature023[i] + trial2_acc_feature023[i] + trial3_acc_feature023[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1,3,4'] = trial_mean_acc_feature023
    trial_mean_acc_features_feature3['f 1,3,4'] = trial_mean_acc_feature023

    trial1_acc_feature123 = [47.35, 61.33, 70.73, 80.03, 82.57, 85.99, 87.57, 88.86, 89.63, 89.98]
    trial2_acc_feature123 = [49.44, 62.95, 73.58, 81.11, 83.18, 86.32, 87.48, 88.9, 89.87, 90.06]
    trial3_acc_feature123 = [47.38, 60.81, 70.02, 78.72, 81.93, 85.1, 86.68, 88.41, 89.03, 89.04]
    trial_mean_acc_feature123 = [
        (trial1_acc_feature123[i] + trial2_acc_feature123[i] + trial3_acc_feature123[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 2,3,4'] = trial_mean_acc_feature123
    trial_mean_acc_features_feature3['f 2,3,4'] = trial_mean_acc_feature123

    trial1_acc_feature01 = [45.94, 55.08, 63.63, 70.87, 76.16, 81.09, 83.37, 84.94, 86.57, 87.53]
    trial2_acc_feature01 = [45.21, 53.33, 62.68, 70.37, 79.01, 82.87, 84.27, 86.07, 87.11, 87.41]
    trial3_acc_feature01 = [47.5, 54.06, 63.05, 71.03, 77.33, 81.82, 83.77, 84.99, 86.84, 87.63]
    trial_mean_acc_feature01 = [
        (trial1_acc_feature01[i] + trial2_acc_feature01[i] + trial3_acc_feature01[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1,2'] = trial_mean_acc_feature01
    trial_mean_acc_features_feature2['f 1,2']=trial_mean_acc_feature01

    trial1_acc_feature02 = [48.66, 58.38, 65.61, 71.69, 78.95, 83.19, 84.79, 86.56, 87.63, 88.44]
    trial2_acc_feature02 = [46.95, 57.88, 67.29, 72.64, 79.76, 83.66, 85.55, 87.13, 88.28, 89.06]
    trial3_acc_feature02 = [45.83, 54.31, 63.81, 70.86, 77.39, 82.96, 85.42, 86.05, 87.31, 88.05]
    trial_mean_acc_feature02 = [
        (trial1_acc_feature02[i] + trial2_acc_feature02[i] + trial3_acc_feature02[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1,3'] = trial_mean_acc_feature02
    trial_mean_acc_features_feature2['f 1,3'] = trial_mean_acc_feature02

    trial1_acc_feature12 = [47.52, 58.38, 67.63, 73.77, 79.21, 83.87, 85.3, 86.76, 87.5, 88.39]
    trial2_acc_feature12 = [46.76, 56.75, 63.63, 71.56, 76.89, 82.75, 84.94, 86.51, 87.73, 88.37]
    trial3_acc_feature12 = [46.6, 54.81, 65.59, 72.87, 78.94, 83.16, 85.24, 86.68, 87.62, 88.19]
    trial_mean_acc_feature12 = [
        (trial1_acc_feature12[i] + trial2_acc_feature12[i] + trial3_acc_feature12[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 2,3'] = trial_mean_acc_feature12
    trial_mean_acc_features_feature2['f 2,3'] = trial_mean_acc_feature12

    trial1_acc_feature03 = [48.44, 62.15, 69.85, 79.34, 83.02, 85.9, 87.45, 88.95, 89.75, 90.04]
    trial2_acc_feature03 = [48.37, 61.67, 71.02, 79.13, 83.1, 86.51, 87.45, 89.51, 89.62, 90.19]
    trial3_acc_feature03 = [42.93, 55.84, 68.93, 77.6, 81.79, 84.78, 87.38, 88.77, 89.82, 90.03]
    trial_mean_acc_feature03 = [
        (trial1_acc_feature03[i] + trial2_acc_feature03[i] + trial3_acc_feature03[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1,4'] = trial_mean_acc_feature03
    trial_mean_acc_features_feature2['f 1,4'] = trial_mean_acc_feature03

    trial1_acc_feature13 = [47.43, 63.12, 71.87, 80.43, 82.74, 86.48, 87.86, 88.46, 90.06, 90.17]
    trial2_acc_feature13 = [46.57, 59.92, 69.46, 77.99, 81.69, 84.98, 87.27, 88.56, 89.43, 89.92]
    trial3_acc_feature13 = [46.95, 61.3, 72.7, 80.39, 83.49, 86.23, 87.76, 88.89, 89.77, 90.05]
    trial_mean_acc_feature13 = [
        (trial1_acc_feature13[i] + trial2_acc_feature13[i] + trial3_acc_feature13[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 2,4'] = trial_mean_acc_feature13
    trial_mean_acc_features_feature2['f 2,4'] = trial_mean_acc_feature13

    trial1_acc_feature23 = [49.84, 62.64, 71.81, 80.13, 83.54, 86.29, 87.67, 88.74, 89.54, 89.33]
    trial2_acc_feature23 = [47.75, 62.3, 71.53, 79.94, 83.43, 86.24, 87.22, 88.81, 89.06, 89.84]
    trial3_acc_feature23 = [43.51, 58.19, 69.64, 78.51, 81.9, 85.09, 87.81, 88.65, 89.65, 90.13]
    trial_mean_acc_feature23 = [
        (trial1_acc_feature23[i] + trial2_acc_feature23[i] + trial3_acc_feature23[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 3,4'] = trial_mean_acc_feature23
    trial_mean_acc_features_feature2['f 3,4'] = trial_mean_acc_feature23

    trial1_acc_feature3 = [47.43, 61.49, 71.17, 80.2, 83.14, 85.69, 87.94, 88.59, 89.38, 89.99]
    trial2_acc_feature3 = [48.94, 63.08, 72.64, 80.66, 82.67, 86.15, 87.85, 88.7, 89.63, 90.27]
    trial3_acc_feature3 = [45.44, 59.43, 69.65, 78.8, 82.93, 85.88, 87.15, 88.82, 90.1, 90.65]
    trial_mean_acc_feature3 = [
        (trial1_acc_feature3[i] + trial2_acc_feature3[i] + trial3_acc_feature3[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 4'] = trial_mean_acc_feature3
    trial_mean_acc_features_feature1['f 4'] = trial_mean_acc_feature3

    trial1_acc_feature2 = [46.15, 53.75, 62.2, 68.82, 78.06, 82.44, 84.55, 85.97, 87.93, 88.48]
    trial2_acc_feature2 = [42.47, 52.1, 62.73, 72.69, 78.71, 82.99, 84.53, 86.2, 87.66, 88.76]
    trial3_acc_feature2 = [42.17, 50.68, 59.53, 69.4, 76.87, 81.51, 84.06, 85.52, 86.78, 87.25]
    trial_mean_acc_feature2 = [
        (trial1_acc_feature2[i] + trial2_acc_feature2[i] + trial3_acc_feature2[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 3'] = trial_mean_acc_feature2
    trial_mean_acc_features_feature1['f 3'] = trial_mean_acc_feature2

    trial1_acc_feature1 = [46.44, 55.86, 65.04, 71.95, 78.67, 81.94, 83.89, 85.21, 86.44, 87.56]
    trial2_acc_feature1 = [47.89, 55.1, 62.86, 70.02, 78.22, 81.15, 83.23, 85.1, 86.35, 87.42]
    trial3_acc_feature1 = [48.39, 56.18, 65.83, 72.12, 78.98, 81.71, 83.95, 85.14, 86.22, 87.41]
    trial_mean_acc_feature1 = [
        (trial1_acc_feature1[i] + trial2_acc_feature1[i] + trial3_acc_feature1[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 2'] = trial_mean_acc_feature1
    trial_mean_acc_features_feature1['f 2'] = trial_mean_acc_feature1

    trial1_acc_feature0 = [43.42, 51.38, 60.25, 69.85, 76.91, 79.7, 83.22, 84.73, 86.2, 86.85]
    trial2_acc_feature0 = [48.43, 56.98, 63.47, 70.14, 77.01, 80.35, 82.92, 84.53, 85.72, 86.59]
    trial3_acc_feature0 = [48.99, 58.48, 68.36, 74.15, 77.91, 81.81, 83.77, 85.49, 87.04, 87.73]
    trial_mean_acc_feature0 = [
        (trial1_acc_feature0[i] + trial2_acc_feature0[i] + trial3_acc_feature0[i]) / 3 for i in range(0, 10)]
    trial_mean_acc_features['f 1'] = trial_mean_acc_feature0
    trial_mean_acc_features_feature1['f 1'] = trial_mean_acc_feature0


    trial_mean_acc_features_key = list(trial_mean_acc_features.keys())
    trial_mean_acc_features_value = list(trial_mean_acc_features.values())

    trial_mean_acc_features3_key = list(trial_mean_acc_features_feature3.keys())
    trial_mean_acc_features3_value = list(trial_mean_acc_features_feature3.values())

    trial_mean_acc_features2_key = list(trial_mean_acc_features_feature2.keys())
    trial_mean_acc_features2_value = list(trial_mean_acc_features_feature2.values())

    trial_mean_acc_features1_key = list(trial_mean_acc_features_feature1.keys())
    trial_mean_acc_features1_value = list(trial_mean_acc_features_feature1.values())

    #Time cost

    trial1_time_feature0123 = [2.6577300071716308, 5.335939625898997, 8.115179006258646, 10.798736389478048, 12.327481357256572, 15.306232229868572, 17.647127350171406, 21.35555650393168, 23.433697732289634, 26.894384217262267]
    trial2_time_feature0123 = [2.4056554317474363, 5.06564215819041, 7.310097138086955, 10.7414755264918, 13.010966996351877, 15.508964888254802, 17.40419728755951, 19.60448964834213, 23.637927532196045, 26.867488467693327]
    trial3_time_feature0123 = [2.606064558029175, 5.117868900299072, 7.743092250823975, 10.360012821356456, 11.327342510223389, 14.872857598463694, 18.81498151620229, 21.136036590735117, 23.941779673099518, 25.748588009675345]
    trial_mean_time_feature0123 = sum([(trial1_time_feature0123[i] + trial2_time_feature0123[i] + trial3_time_feature0123[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,2,3,4']=trial_mean_time_feature0123
    trial_mean_time_features_feature3['f 1,2,3,4']=trial_mean_time_feature0123
    trial_mean_time_features_feature2['f 1,2,3,4'] = trial_mean_time_feature0123
    trial_mean_time_features_feature1['f 1,2,3,4'] = trial_mean_time_feature0123

    trial1_time_feature012 = [2.4007288495699566, 5.309695669015249, 8.066733451684316, 9.789838707447052, 13.149123227596283, 15.412629159291585, 17.329690011342368, 20.66565339167913, 23.893751907348634, 25.224287442366283]
    trial2_time_feature012 = [2.3945579131444297, 5.009990394115448, 7.9128448367118835, 10.850939929485321, 13.444391079743703, 14.746567602952322, 17.172255035241445, 20.486111915111543, 23.787155854701997, 26.8556285738945]
    trial3_time_feature012 = [2.4128785292307535, 4.797274219989776, 7.807326833407084, 10.516408006350199, 13.232375701268515, 15.268672271569569, 18.26403412818909, 21.23996640841166, 21.066751646995545, 26.86742406686147]
    trial_mean_time_feature012 = sum([
        (trial1_time_feature012[i] + trial2_time_feature012[i] + trial3_time_feature012[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,2,3']=trial_mean_time_feature012
    trial_mean_time_features_feature3['f 1,2,3']=trial_mean_time_feature012

    trial1_time_feature013 = [2.730805742740631, 5.427584914366404, 7.8875861008962, 10.62018240292867, 13.370141514142354, 15.937201348940532, 17.291286023457847, 20.865663905938465, 23.422136441866556, 26.71342135667801]
    trial2_time_feature013 = [2.5691354473431907, 5.180234789848328, 7.637486755847931, 10.812549265225728, 13.169064223766327, 16.163757932186126, 17.99549123843511, 21.402850421269736, 24.05370899836222, 26.786947770913443]
    trial3_time_feature013 = [2.386166548728943, 5.245085990428924, 8.109891537825266, 10.626919253667195, 13.146520634492239, 16.058935372034707, 18.72966115474701, 20.765909206867217, 23.155802675088246, 26.005555550257366]
    trial_mean_time_feature013 = sum([
        (trial1_time_feature013[i] + trial2_time_feature013[i] + trial3_time_feature013[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,2,4']=trial_mean_time_feature013
    trial_mean_time_features_feature3['f 1,2,4']=trial_mean_time_feature013

    trial1_time_feature023 = [2.5463711539904277, 5.311703372001648, 7.8017171422640486, 9.575130581855774, 12.789659861723582, 14.47649044195811, 18.11628026564916, 19.913264087835948, 23.813901221752168, 26.536199831962584]
    trial2_time_feature023 = [2.7269799153010053, 5.374827015399933, 7.6509947061538695, 10.296533989906312, 12.018099208672842, 15.80482869942983, 18.91042618751526, 20.743589647610982, 24.03661764462789, 27.241055126984914]
    trial3_time_feature023 = [2.6775379300117494, 5.172347124417623, 7.793867524464925, 10.650024104118348, 13.645113770167033, 15.96622314453125, 18.58206792672475, 20.063354698816934, 22.5622456073761, 26.322339022159575]
    trial_mean_time_feature023 = sum([
        (trial1_time_feature023[i] + trial2_time_feature023[i] + trial3_time_feature023[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,3,4']=trial_mean_time_feature023
    trial_mean_time_features_feature3['f 1,3,4']=trial_mean_time_feature023

    trial1_time_feature123 = [2.424927230676015, 4.810205519199371, 7.962366692225138, 9.805800791581472, 12.258497349421184, 16.14544363816579, 18.589908504486083, 21.48101978302002, 24.342422457536063, 26.189729022979737]
    trial2_time_feature123 = [2.496358605225881, 4.886036662260691, 7.986460415522258, 9.599675464630128, 13.294041113058727, 15.356745239098867, 18.73572082122167, 20.682476818561554, 23.66280425786972, 26.669721575578055]
    trial3_time_feature123 = [2.5251232584317527, 4.771351385116577, 7.2564159234364825, 10.185938119888306, 12.953105445702871, 15.745243724187215, 18.648956207434335, 21.101587224006654, 24.31739611228307, 27.18476949930191]
    trial_mean_time_feature123 = sum([
        (trial1_time_feature123[i] + trial2_time_feature123[i] + trial3_time_feature123[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 2,3,4']=trial_mean_time_feature123
    trial_mean_time_features_feature3['f 2,3,4']=trial_mean_time_feature123

    trial1_time_feature01 = [2.4700045784314475, 5.423065344492595, 7.122748891512553, 9.49255359172821, 13.11244174639384, 15.604230924447377, 17.141841189066568, 21.443360944588978, 23.96862239440282, 26.406481858094534]
    trial2_time_feature01 = [2.7258653044700623, 5.131121365229289, 8.071965499718983, 10.414421387513478, 13.487719023227692, 14.408841808636984, 17.695642264684043, 19.641792631149293, 24.03412605524063, 26.67887379725774]
    trial3_time_feature01 = [2.705409348011017, 5.185869399706522, 7.4368682106335955, 9.602606352170309, 12.724880258242289, 15.17641357978185, 18.322388100624085, 21.347530408700308, 23.395344813664753, 26.143969452381135]
    trial_mean_time_feature01 = sum([
        (trial1_time_feature01[i] + trial2_time_feature01[i] + trial3_time_feature01[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,2']=trial_mean_time_feature01
    trial_mean_time_features_feature2['f 1,2']=trial_mean_time_feature01

    trial1_time_feature02 = [2.5704296032587686, 4.97302847703298, 8.075918487707774, 10.812007029851278, 13.321785016854603, 14.16782337029775, 18.684712890783945, 20.710833978652953, 21.96040666103363, 26.554674899578096]
    trial2_time_feature02 = [2.3668613910675047, 5.373975257078807, 7.487341765562693, 9.472144174575806, 13.259300903479259, 15.411866188049316, 18.501963639259337, 21.10637197494507, 24.096360250314078, 25.37475637594859]
    trial3_time_feature02 = [2.728411789735158, 5.3933874050776165, 7.642868979771932, 10.03710832198461, 12.755983368555706, 14.851218283176422, 17.870639419555665, 21.223779233296714, 23.856275153160095, 26.59652174313863]
    trial_mean_time_feature02 = sum([
        (trial1_time_feature02[i] + trial2_time_feature02[i] + trial3_time_feature02[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,3'] = trial_mean_time_feature02
    trial_mean_time_features_feature2['f 1,3'] = trial_mean_time_feature02

    trial1_time_feature12 = [2.6865557273228964, 5.201448575655619, 7.064867043495179, 10.449074188868204, 13.149392759799957, 13.82042019367218, 18.08086861371994, 20.320165661970773, 23.60150825182597, 25.615404017766316]
    trial2_time_feature12 = [2.647713593641917, 5.1592787106831866, 8.023331705729166, 9.844128517309825, 12.476699435710907, 15.856632347901662, 18.513715692361195, 20.561277520656585, 23.028202748298646, 26.22421214580536]
    trial3_time_feature12 = [2.353299105167389, 5.352306699752807, 8.0344442486763, 10.347263212998708, 12.706427784760793, 15.793472560246785, 18.145924250284832, 21.005658336480458, 23.598105092843372, 25.62400751511256]
    trial_mean_time_feature12 = sum([
        (trial1_time_feature12[i] + trial2_time_feature12[i] + trial3_time_feature12[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 2,3']=trial_mean_time_feature12
    trial_mean_time_features_feature2['f 2,3'] = trial_mean_time_feature12

    trial1_time_feature03 = [2.7556908170382184, 4.774810866514842, 8.142385224501291, 9.711344468593598, 13.248491505781809, 13.445964515209198, 18.667864994208017, 21.65089405377706, 24.146846910317738, 26.94034481048584]
    trial2_time_feature03 = [2.587923268477122, 5.262073993682861, 7.982017918427785, 10.274946669737497, 13.252634382247924, 15.257462612787883, 19.085290014743805, 20.23434514204661, 24.16537397702535, 26.508557617664337]
    trial3_time_feature03 = [2.7415105581283568, 5.487672579288483, 7.9499323010444645, 10.316262837251028, 13.454401850700378, 16.24689301252365, 19.040468724568687, 21.52108302513758, 22.246593403816224, 25.37997330824534]
    trial_mean_time_feature03 = sum([
        (trial1_time_feature03[i] + trial2_time_feature03[i] + trial3_time_feature03[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1,4']=trial_mean_time_feature03
    trial_mean_time_features_feature2['f 1,4'] = trial_mean_time_feature03

    trial1_time_feature13 = [2.6013910015424093, 5.22839005390803, 8.061638732751211, 10.8067831436793, 13.496167159080505, 16.263864688078563, 17.784911978244782, 21.46769207715988, 24.249732180436453, 25.964209910233816]
    trial2_time_feature13 = [2.7196182449658712, 5.239992439746857, 7.804321368535359, 10.891478371620178, 13.55197517077128, 16.185799956321716, 18.89455771446228, 20.906588411331178, 23.5577055255572, 26.53378987709681]
    trial3_time_feature13 = [2.699138907591502, 5.251582940419515, 8.210694909095764, 10.900817294915518, 13.4574209690094, 16.058947837352754, 18.900108432769777, 21.02073702017466, 23.33221914768219, 27.06363954146703]
    trial_mean_time_feature13 = sum([
        (trial1_time_feature13[i] + trial2_time_feature13[i] + trial3_time_feature13[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 2,4']=trial_mean_time_feature13
    trial_mean_time_features_feature2['f 2,4'] = trial_mean_time_feature13

    trial1_time_feature23 = [2.609572347005208, 5.128187843163809, 7.588878035545349, 10.853768869241078, 13.033701392014821, 15.669457280635834, 18.74513647556305, 20.211669651667275, 23.01460288365682, 26.557029247283936]
    trial2_time_feature23 = [2.448874469598134, 5.379959722359975, 7.124969470500946, 9.80956336259842, 12.991429674625397, 16.037735124429066, 18.23502998749415, 20.939772856235503, 22.509366182486215, 26.670441269874573]
    trial3_time_feature23 = [2.606058418750763, 5.117141707738241, 7.754590388139089, 10.474609204133351, 13.43794881105423, 15.16740821202596, 18.533755377928415, 20.52669178644816, 23.410280764102936, 24.49979159037272]
    trial_mean_time_feature23 = sum([
        (trial1_time_feature23[i] + trial2_time_feature23[i] + trial3_time_feature23[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 3,4']=trial_mean_time_feature23
    trial_mean_time_features_feature2['f 3,4'] = trial_mean_time_feature23

    trial1_time_feature3 = [2.6182073831558226, 4.66362946430842, 7.670720259348552, 10.600845396518707, 13.366521859169007, 14.76645059188207, 18.1390384833018, 20.844265321890514, 23.472656754652657, 26.342110188802085]
    trial2_time_feature3 = [2.6831104795138043, 4.890668427944183, 7.787248528003692, 10.55996474424998, 13.149452857176463, 13.526703615983328, 15.172175614039103, 20.575668966770174, 23.23371106783549, 25.255909136931102]
    trial3_time_feature3 = [2.4822761019070945, 5.151100337505341, 7.42401415904363, 10.459452760219573, 13.189911909898122, 15.911228621006012, 14.862787274519603, 19.34717763264974, 22.669207898775735, 26.24051774740219]
    trial_mean_time_feature3 = sum([
        (trial1_time_feature3[i] + trial2_time_feature3[i] + trial3_time_feature3[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 4'] = trial_mean_time_feature3
    trial_mean_time_features_feature1['f 4'] = trial_mean_time_feature3

    trial1_time_feature2 = [2.0705564578374225, 5.252754318714142, 7.035783648490906, 10.138147779305775, 13.283046464125315, 15.00072325070699, 17.924177408218384, 21.061644641558328, 21.924203221003214, 23.390940010547638]
    trial2_time_feature2 = [2.5600298086802167, 4.722093645731608, 7.782012124856313, 10.582661342620849, 12.764654846986135, 15.236761864026388, 16.659020149707793, 21.290998951594034, 23.80547033150991, 26.395923614501953]
    trial3_time_feature2 = [2.671622467041016, 4.752454928557078, 7.584345360596974, 10.298905503749847, 13.349909079074859, 15.842946358521779, 18.134767742951713, 20.41292488972346, 23.017874618371327, 26.0445063829422]
    trial_mean_time_feature2 = sum([
        (trial1_time_feature2[i] + trial2_time_feature2[i] + trial3_time_feature2[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 3'] = trial_mean_time_feature2
    trial_mean_time_features_feature1['f 3'] = trial_mean_time_feature2

    trial1_time_feature1 = [2.616826093196869, 5.3403481920560205, 7.544566738605499, 10.512454311052958, 13.234067444006602, 15.677615229288737, 18.296463080247243, 21.03596107165019, 23.66402986049652, 26.14702776670456]
    trial2_time_feature1 = [2.6936114470163983, 5.054953217506409, 7.672989602883657, 10.641360370318095, 12.966228071848551, 15.549025849501293, 18.37947733402252, 19.971469116210937, 24.038696360588073, 26.686225350697836]
    trial3_time_feature1 = [2.6687647859255472, 5.310221298535665, 8.061503009001415, 10.593186791737875, 13.400991070270539, 15.202443146705628, 17.675267124176024, 20.74849929412206, 23.863072343667348, 26.28244682153066]
    trial_mean_time_feature1 = sum([
        (trial1_time_feature1[i] + trial2_time_feature1[i] + trial3_time_feature1[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 2'] = trial_mean_time_feature1
    trial_mean_time_features_feature1['f 2'] = trial_mean_time_feature1

    trial1_time_feature0 = [2.3861873904863993, 5.383748348553976, 7.120261927445729, 10.463186343510946, 13.186426277955373, 16.01784055630366, 16.204687225818635, 20.87408001422882, 23.989763152599334, 26.169339485963185]
    trial2_time_feature0 = [2.719353365898132, 5.362282963593801, 8.134587260087331, 10.532935551802318, 13.444056912263234, 16.08706507285436, 18.69310720761617, 20.38298803170522, 22.341615239779156, 21.66807961066564]
    trial3_time_feature0 = [2.653677988052368, 5.320750892162323, 7.982435524463654, 10.78880288998286, 13.054594016075134, 14.923098556200664, 17.875215029716493, 20.945593444506326, 22.233200132846832, 25.21337372859319]
    trial_mean_time_feature0 = sum([
        (trial1_time_feature0[i] + trial2_time_feature0[i] + trial3_time_feature0[i]) / 3 for i in range(0, 10)])
    trial_mean_time_features['f 1'] = trial_mean_time_feature0
    trial_mean_time_features_feature1['f 1'] = trial_mean_time_feature0

    trial_mean_time_features_sorted=sorted(trial_mean_time_features.items(),key=operator.itemgetter(1))
    trial_mean_time_features3_sorted = sorted(trial_mean_time_features_feature3.items(), key=operator.itemgetter(1))
    trial_mean_time_features2_sorted = sorted(trial_mean_time_features_feature2.items(), key=operator.itemgetter(1))
    trial_mean_time_features1_sorted = sorted(trial_mean_time_features_feature1.items(), key=operator.itemgetter(1))

    #plot

    ax1 = fig.add_subplot(2, 4, 1)
    ax1.set_title("Test acc")
    for i in range(0, len(trial_mean_acc_features)):
        ax1.plot(x, trial_mean_acc_features_value[i],
                label=str(trial_mean_acc_features_key[i]))

    ax1.set_xlabel("number of labeled image")
    ax1.set_ylabel("Accuracy")
    ax1.legend()
    plt.grid(True)

    ax2 = fig.add_subplot(2, 4, 2)
    ax2.set_title("Total time")
    for i in range(0,len(trial_mean_time_features_sorted)):
        ax2.bar(str(trial_mean_time_features_sorted[i][0]), trial_mean_time_features_sorted[i][1], label=str(trial_mean_time_features_sorted[i][0]))
    ax2.set_xlabel("Features selected")
    ax2.set_ylabel("Time")
    ax2.axes.xaxis.set_visible(False)
    ax2.legend()
    plt.grid(True)

    ax3 = fig.add_subplot(2, 4, 3)
    ax3.set_title("Test acc")
    for i in range(0, len(trial_mean_acc_features_feature3)):
        ax3.plot(x, trial_mean_acc_features3_value[i],
                label=str(trial_mean_acc_features3_key[i]))

    ax3.set_xlabel("number of labeled image")
    ax3.set_ylabel("Accuracy")
    ax3.legend()
    plt.grid(True)

    ax4 = fig.add_subplot(2, 4, 4)
    ax4.set_title("Total time")
    for i in range(0,len(trial_mean_time_features3_sorted)):
        ax4.bar(str(trial_mean_time_features3_sorted[i][0]), trial_mean_time_features3_sorted[i][1], label=str(trial_mean_time_features3_sorted[i][0]))
    ax4.set_xlabel("Features selected")
    ax4.set_ylabel("Time")
    ax4.legend()
    ax4.axes.xaxis.set_visible(False)
    plt.grid(True)

    ax5 = fig.add_subplot(2, 4, 5)
    ax5.set_title("Test acc")
    for i in range(0, len(trial_mean_acc_features_feature2)):
        ax5.plot(x, trial_mean_acc_features2_value[i],
                label=str(trial_mean_acc_features2_key[i]))

    ax5.set_xlabel("number of labeled image")
    ax5.set_ylabel("Accuracy")
    ax5.legend()
    plt.grid(True)

    ax6 = fig.add_subplot(2, 4, 6)
    ax6.set_title("Total time")
    for i in range(0,len(trial_mean_time_features2_sorted)):
        ax6.bar(str(trial_mean_time_features2_sorted[i][0]), trial_mean_time_features2_sorted[i][1], label=str(trial_mean_time_features2_sorted[i][0]))
    ax6.set_xlabel("Features selected")
    ax6.set_ylabel("Time")
    ax6.legend()
    ax6.axes.xaxis.set_visible(False)
    plt.grid(True)

    ax7 = fig.add_subplot(2, 4, 7)
    ax7.set_title("Test acc")
    for i in range(0, len(trial_mean_acc_features_feature1)):
        ax7.plot(x, trial_mean_acc_features1_value[i], label=str(trial_mean_acc_features1_key[i]))

    ax7.set_xlabel("number of labeled image")
    ax7.set_ylabel("Accuracy")
    ax7.legend()
    plt.grid(True)

    ax8 = fig.add_subplot(2, 4, 8)
    ax8.set_title("Total time")
    for i in range(0,len(trial_mean_time_features1_sorted)):
        ax8.bar(str(trial_mean_time_features1_sorted[i][0]), trial_mean_time_features1_sorted[i][1], label=str(trial_mean_time_features1_sorted[i][0]))
    ax8.set_xlabel("Features selected")
    ax8.set_ylabel("Time")
    ax8.legend()
    ax8.axes.xaxis.set_visible(False)
    plt.grid(True)


    plt.show()

# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    LearningLoss()
