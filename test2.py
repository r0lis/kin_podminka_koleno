import pandas as pd
import matplotlib.pyplot as plt

T1 = pd.read_csv("kin_podminka_1.txt", skiprows=4, delimiter='\t')
T2 = pd.read_csv("kin_podminka_2.txt", skiprows=4, delimiter='\t')

array = T1.to_numpy()
array2 = T2.to_numpy()

y_os = array[:, 13]
os_x = array[:, 0]
err1 = array[:, 14]
y_os2 = array2[:, 13]
os_x2 = array2[:, 0]
err2 = array2[:, 15]

plt.figure(1)
plt.plot(os_x, y_os, "b")
e = plt.errorbar(os_x, y_os, err1)
plt.title("L_sagital")
plt.xlabel("% chůz.cykl")
plt.ylabel("extenze-flexe")
plt.plot(os_x2, y_os2, "r")
e2 = plt.errorbar(os_x2, y_os2, err2)
plt.legend(["Podmínka_1", "Podmínka_2"])
plt.show()

y_os = array[:, 15]
os_x = array[:, 0]
err1 = array[:, 16]
y_os2 = array2[:, 15]
os_x2 = array2[:, 0]
err2 = array2[:, 16]

plt.figure(1)
plt.plot(os_x, y_os, "b")
e = plt.errorbar(os_x, y_os, err1)
plt.title("L_frontal")
plt.xlabel("% chůz.cykl")
plt.ylabel("abdukce-addukce")
plt.plot(os_x2, y_os2, "r")
e2 = plt.errorbar(os_x2, y_os2, err2)
plt.legend(["Podmínka_1", "Podmínka_2"])
plt.show()

y_os = array[:, 17]
os_x = array[:, 0]
err1 = array[:, 18]
y_os2 = array2[:, 17]
os_x2 = array2[:, 0]
err2 = array2[:, 18]

plt.figure(1)
plt.plot(os_x, y_os, "b")
e = plt.errorbar(os_x, y_os, err1)
plt.title("L_transversal")
plt.xlabel("% chůz.cykl")
plt.ylabel("int.rot-ext.rot")
plt.plot(os_x2, y_os2, "r")
e2 = plt.errorbar(os_x2, y_os2, err2)
plt.legend(["Podmínka_1", "Podmínka_2"])
plt.show()

y_os = array[:, 25]
os_x = array[:, 0]
err1 = array[:, 26]
y_os2 = array2[:, 25]
os_x2 = array2[:, 0]
err2 = array2[:, 26]

plt.figure(1)
plt.plot(os_x, y_os, "b")
e = plt.errorbar(os_x, y_os, err1)
plt.title("P_sagital")
plt.xlabel("% chůz.cykl")
plt.ylabel("extenze-flexe")
plt.plot(os_x2, y_os2, "r")
e2 = plt.errorbar(os_x2, y_os2, err2)
plt.legend(["Podmínka_1", "Podmínka_2"])
plt.show()


y_os = array[:, 27]
os_x = array[:, 0]
err1 = array[:, 28]
y_os2 = array2[:, 27]
os_x2 = array2[:, 0]
err2 = array2[:, 28]

plt.figure(1)
plt.plot(os_x, y_os, "b")
e = plt.errorbar(os_x, y_os, err1)
plt.title("P_frontal")
plt.xlabel("% chůz.cykl")
plt.ylabel("abdukce-addukce")
plt.plot(os_x2, y_os2, "r")
e2 = plt.errorbar(os_x2, y_os2, err2)
plt.legend(["Podmínka_1", "Podmínka_2"])
plt.show()


y_os = array[:, 29]
os_x = array[:, 0]
err1 = array[:, 30]
y_os2 = array2[:, 29]
os_x2 = array2[:, 0]
err2 = array2[:, 30]

plt.figure(1)
plt.plot(os_x, y_os, "b")
e = plt.errorbar(os_x, y_os, err1)
plt.title("P_transversal")
plt.xlabel("% chůz.cykl")
plt.ylabel("int.rot-ext.rot")
plt.plot(os_x2, y_os2, "r")
e2 = plt.errorbar(os_x2, y_os2, err2)
plt.legend(["Podmínka_1", "Podmínka_2"])
plt.show()