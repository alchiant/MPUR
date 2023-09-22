import math

N100 = 6 / 100

# calculate and set individual productivity
managerProductivity =           [0.5 + N100,
                                 0.9 - N100,
                                 0.3 + N100,
                                 0.85]
lawyerProductivity =            [0.75,
                                 0.25 + 2 * N100,
                                 0.45 + N100,
                                 0.95 - N100]
economistProductivity =         [0.5 + N100,
                                 0.9 - N100,
                                 0.3 + 2 * N100,
                                 0.85]
engineerProductivity =          [0.65,
                                 0.05 + 3 * N100,
                                 0.35 + N100,
                                 0.85 - N100]
programmerProductivity =        [0.6,
                                 0.2 + 2 * N100,
                                 0.5 + N100,
                                 1.0 - N100]

# set manager factors - first index is the manager, second is the specialist
lawyerManagerEfficiency =       [[0.8, 0.3, 0.2, 0.5],
                                 [0.9, 0.6, 0.4, 0.6],
                                 [0.3, 0.3, 0.7, 0.7],
                                 [0.7, 0.7, 0.2, 0.3]]
economistManagerEfficiency =    [[0.1, 0.6, 0.6, 0.3],
                                 [0.8, 0.2, 0.2, 0.5],
                                 [0.5, 0.5, 0.3, 0.7],
                                 [0.4, 0.6, 0.5, 0.6]]
engineerManagerEfficiency =     [[0.1, 0.6, 0.6, 0.3],
                                 [0.8, 0.2, 0.2, 0.5],
                                 [0.5, 0.5, 0.3, 0.7],
                                 [0.4, 0.6, 0.5, 0.6]]
programmerManagerEfficiency =   [[0.5, 0.5, 0.6, 0.7],
                                 [0.4, 0.6, 0.6, 0.2],
                                 [0.3, 0.6, 0.4, 0.3],
                                 [0.2, 0.5, 0.4, 0.5]]

def calculateXi_(xi, yi):
    return (xi * (1 - yi)) / ((xi * (1 - yi)) + (yi * (1 - xi)))

def calculateXiStar(xi, yi, x0):
    xi_ = calculateXi_(xi, yi)
    term1 = xi_ * (1 - x0)
    term2 = x0 * (1 - xi_)
    xistar = 0.5 * math.sqrt((term1 / term2) + (term2 / term1) - 2)
    if xi_ >= 0.5:
        return xistar
    else:
        return -xistar

def calculateR0(i_man, i_law, i_eco, i_eng, i_pro):
    x0 = managerProductivity[i_man]
    xstarsum = (calculateXiStar(lawyerProductivity[i_law], lawyerManagerEfficiency[i_man][i_law], x0)  
             +  calculateXiStar(economistProductivity[i_eco], economistManagerEfficiency[i_man][i_eco], x0)
             +  calculateXiStar(engineerProductivity[i_eng], engineerManagerEfficiency[i_man][i_eng], x0)
             +  calculateXiStar(programmerProductivity[i_pro], programmerManagerEfficiency[i_man][i_pro], x0))
    return 0.5 + (xstarsum / (2 * math.sqrt((xstarsum * xstarsum) + 1)))

def calculateP(i_man, i_law, i_eco, i_eng, i_pro):
    r0 = calculateR0(i_man, i_law, i_eco, i_eng, i_pro)
    x0 = managerProductivity[i_man]
    return (r0 * x0) / ((r0 * x0) + (1 - r0) * (1 - x0))

best_lawyer_xi_ = 0
best_economist_xi_ = 0
best_engineer_xi_ = 0
best_programmer_xi_ = 0
best_lawyer_xi_star = 0
best_economist_xi_star = 0
best_engineer_xi_star = 0
best_programmer_xi_star = 0

for i_man in range(4):
    x0 = managerProductivity[i_man]
    for i_law in range(4):
        xi_ = calculateXi_(lawyerProductivity[i_law], lawyerManagerEfficiency[i_man][i_law])
        if xi_ > best_lawyer_xi_:
            best_lawyer_xi_ = xi_
            mostProductiveLawyerPair = [i_man, i_law]
        xi_star = calculateXiStar(lawyerProductivity[i_law], lawyerManagerEfficiency[i_man][i_law], x0)
        if xi_star > best_lawyer_xi_star:
            best_lawyer_xi_star = xi_star
            mostEffectiveLawyerPair = [i_man, i_law]
    for i_eco in range(4):
        xi_ = calculateXi_(economistProductivity[i_eco], economistManagerEfficiency[i_man][i_eco])
        if xi_ > best_economist_xi_:
            best_economist_xi_ = xi_
            mostProductiveEconomistPair = [i_man, i_eco]
        xi_star = calculateXiStar(economistProductivity[i_eco], economistManagerEfficiency[i_man][i_eco], x0)
        if xi_star > best_economist_xi_star:
            best_economist_xi_star = xi_star
            mostEffectiveEconomistPair = [i_man, i_eco]
    for i_eng in range(4):
        xi_ = calculateXi_(engineerProductivity[i_eng], engineerManagerEfficiency[i_man][i_eng])
        if xi_ > best_engineer_xi_:
            best_engineer_xi_ = xi_
            mostProductiveEngineerPair = [i_man, i_eng]
        xi_star = calculateXiStar(engineerProductivity[i_eng], engineerManagerEfficiency[i_man][i_eng], x0)
        if xi_star > best_engineer_xi_star:
            best_engineer_xi_star = xi_star
            mostEffectiveEngineerPair = [i_man, i_eng]
    for i_pro in range(4):
        xi_ = calculateXi_(programmerProductivity[i_pro], programmerManagerEfficiency[i_man][i_pro])
        if xi_ > best_programmer_xi_:
            best_programmer_xi_ = xi_
            mostProductiveProgrammerPair = [i_man, i_pro]
        xi_star = calculateXiStar(programmerProductivity[i_pro], programmerManagerEfficiency[i_man][i_pro], x0)
        if xi_star > best_programmer_xi_star:
            best_programmer_xi_star = xi_star
            mostEffectiveProgrammerPair = [i_man, i_pro]

print('Most productive manager/lawyer pair:'
    + ' Manager ' + str(mostProductiveLawyerPair[0] + 1)
    + ' Lawyer ' + str(mostProductiveLawyerPair[1] + 1) + ': ' + str(best_lawyer_xi_))
print('Most effective manager/lawyer pair:'
    + ' Manager ' + str(mostEffectiveLawyerPair[0] + 1)
    + ' Lawyer ' + str(mostEffectiveLawyerPair[1] + 1) + ': ' + str(best_lawyer_xi_star))
print('Most productive manager/economist pair:'
    + ' Manager ' + str(mostProductiveEconomistPair[0] + 1)
    + ' Economist ' + str(mostProductiveEconomistPair[1] + 1) + ': ' + str(best_economist_xi_))
print('Most effective manager/economist pair:'
    + ' Manager ' + str(mostEffectiveEconomistPair[0] + 1)
    + ' Economist ' + str(mostEffectiveEconomistPair[1] + 1) + ': ' + str(best_economist_xi_star))
print('Most productive manager/engineer pair:'
    + ' Manager ' + str(mostProductiveEngineerPair[0] + 1)
    + ' Engineer ' + str(mostProductiveEngineerPair[1] + 1) + ': ' + str(best_engineer_xi_))
print('Most effective manager/engineer pair:'
    + ' Manager ' + str(mostEffectiveEngineerPair[0] + 1)
    + ' Engineer ' + str(mostEffectiveEngineerPair[1] + 1) + ': ' + str(best_engineer_xi_star))
print('Most productive manager/programmer pair:'
    + ' Manager ' + str(mostProductiveProgrammerPair[0] + 1)
    + ' Programmer ' + str(mostProductiveProgrammerPair[1] + 1) + ': ' + str(best_programmer_xi_))
print('Most effective manager/programmer pair:'
    + ' Manager ' + str(mostEffectiveProgrammerPair[0] + 1)
    + ' Programmer ' + str(mostEffectiveProgrammerPair[1] + 1) + ': ' + str(best_programmer_xi_star))

best_p = 0

for i_man in range(4):
    for i_law in range(4):
        for i_eco in range(4):
            for i_eng in range(4):
                for i_pro in range(4):
                    p = calculateP(i_man, i_law, i_eco, i_eng, i_pro)
                    if p > best_p:
                        best_p = p
                        best_team = [i_man, i_law, i_eco, i_eng, i_pro]
                        x0 = managerProductivity[i_man]
                        best_law_xi_ = calculateXi_(lawyerProductivity[i_law], lawyerManagerEfficiency[i_man][i_law])
                        best_law_x_star = calculateXiStar(lawyerProductivity[i_pro], lawyerManagerEfficiency[i_man][i_pro], x0)
                        best_eco_xi_ = calculateXi_(economistProductivity[i_law], economistManagerEfficiency[i_man][i_law])
                        best_eco_x_star = calculateXiStar(economistProductivity[i_pro], economistManagerEfficiency[i_man][i_pro], x0)
                        best_eng_xi_ = calculateXi_(engineerProductivity[i_law], engineerManagerEfficiency[i_man][i_law])
                        best_eng_x_star = calculateXiStar(engineerProductivity[i_pro], engineerManagerEfficiency[i_man][i_pro], x0)
                        best_pro_xi_ = calculateXi_(programmerProductivity[i_law], programmerManagerEfficiency[i_man][i_law])
                        best_pro_x_star = calculateXiStar(programmerProductivity[i_pro], programmerManagerEfficiency[i_man][i_pro], x0)

print('')

print('The best team has a productivity of ' + str(p) + ' and is comprised of these members:')
print('Manager ' + str(best_team[0] + 1))
print('Lawyer ' + str(best_team[1] + 1) + ' - xi_: ' + str(best_law_xi_) + ' xi*: ' + str(best_law_x_star))
print('Economist ' + str(best_team[2] + 1) + ' - xi_: ' + str(best_eco_xi_) + ' xi*: ' + str(best_eco_x_star))
print('Engineer ' + str(best_team[3] + 1) + ' - xi_: ' + str(best_eng_xi_) + ' xi*: ' + str(best_eng_x_star))
print('Programmer ' + str(best_team[4] + 1) + ' - xi_: ' + str(best_pro_xi_) + ' xi*: ' + str(best_pro_x_star))
