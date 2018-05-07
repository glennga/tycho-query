from matplotlib import pyplot as plt

c = {
    'q1-ni-3': [0.0032928510476484094, 0.0006944532592847523],
    'q2a-ni-3': [0.8833112317714228, 0.08065389522822365],
    'q2b-ni-3': [0.013505748152370899, 0.005367901599765409],
    'q3-ni-3': [0.010237093946658811, 0.002617266173445302],
    'q4a-ni-3': [0.8781682604603298, 0.046658391211282],
    'q4b-ni-3': [0.013565749374604835, 0.005439534595723085],
    'q5-ni-3': [0.007675607786647258, 0.001450168952226107],

    'q4a-bti-3': [0.8538417516762545, 0.04510117218522853],
    'q4b-bti-3': [0.011636037771446383, 0.004602088733823957],
    'q5-bti-3': [0.005915193966611696, 0.000858881748985823],

    'q1-ni-2': [0.002637954034911499, 0.0011078433694898548],
    'q1-ni-1': [0.00206521924128682, 0.00037728167327796705]
}

n = {
    'q1-ni-3': [1.5757170152848796, 12.31380530251971],
    'q2a-ni-3': [0.0020253124878901432, 0.001086096048290087],
    'q2b-ni-3': [0.010508776357605573, 0.004743660335499862],
    'q3a-ni-3': [0.018133906163733848, 0.10954898503900237],
    'q3b-ni-3': [0.027815536254583453, 0.1475455787743927],
    'q4a-ni-3': [0.0003602192211639538, 0.000815249082152764],
    'q4b-ni-3': [0.008498490802980306, 0.004237151890899335],
    'q5a-ni-3': [0.9672484562847482, 9.159639204173992],
    'q5b-ni-3': [0.8981495416091286, 8.50418097208977],

    'q1-tyc1i-3': [0.000341343209473769, 6.520543358778317e-05],
    'q3a-tyc1i-3': [0.0019460657667933088, 0.000966796761709786],
    'q5a-tyc1i-3': [0.0003368597879395538, 6.319855250250996e-05],

    'q4a-bti-3': [0.0004264583394008999, 0.0009209294219438152],
    'q4b-bti-3': [0.008829952991050738, 0.004394607629841747],
    'q5a-bti-3': [0.0003530136969912388, 0.00030452611586131404],

    'q1-ni-2': [1.3833793584639242, 10.796860523815464],
    'q1-ni-1': [1.3456004863996482, 10.493150782505648],

    # 'q1-ni-3': [1.3131910875211994, 10.242873371470468],
    # 'q2a-ni-3': [0.002313799196941325, 0.001188115567109633],
    # 'q2b-ni-3': [0.011904311178802869, 0.005554798643954421],
    # 'q3a-ni-3': [0.01695104675150243, 0.10453635989884195],
    # 'q3b-ni-3': [0.01968432423639046, 0.11761998187406189],
    # 'q4a-ni-3': [0.000433903336389366, 0.0008417954052906528],
    # 'q4b-ni-3': [0.011201601481783048, 0.006201131158996588],
    # 'q5a-ni-3': [0.9618904258969534, 9.064365885166517],
    # 'q5b-ni-3': [0.9230702970332707, 8.75315472465193],
    #
    # 'q1-tyc1i-3': [0.00039446888505622295, 0.00012163646441988964],
    # 'q3a-tyc1i-3': [0.00196346485767704, 0.0009263502949074313],
    # 'q5a-tyc1i-3': [0.00036222470653504414, 0.0001445163457810881],
    #
    # 'q1-tyci-3': [0.0004022252242672645, 0.0004641230140393104],
    # 'q2a-tyci-3': [0.0021632693272653288, 0.00111774644790932],
    # 'q2b-tyci-3': [0.011435907160568715, 0.00551112881374714],
    # 'q3a-tyci-3': [0.012771906700006433, 0.08026260753113276],
    # 'q3b-tyci-3': [0.002135913493927519, 0.001146872804253935],
    # 'q4a-tyci-3': [0.002135913493927519, 0.001146872804253935],
    # 'q4b-tyci-3': [0.008877609984896976, 0.004316138810125737],
    # 'q5a-tyci-3': [0.7933290537152943, 7.488547185172661],
    # 'q5b-tyci-3': [0.00032704222132010866, 0.00010048520149647994],
    #
    # 'q4a-bttyci-3': [0.0003848578636417656, 0.0006190849257932613],
    # 'q4b-bttyci-3': [0.009121337742439981, 0.0045757954206354715],
    # 'q5a-bttyci-3': [0.0003836459394127208, 0.0004481475934241216],
    # 'q5b-bttyci-3': [0.0004103141878328064, 0.0009066904260155717],
    #
    # 'q1-bttyci-2': [0.0003992393059117162, 0.00010107540500949478],
    # 'q1-bttyci-1': [0.00041146298791511183, 9.593636017404327e-05],
    #
    # 'q4a-bti-3': [0, 0],
    # 'q4b-bti-3': [0, 0],
    # 'q5a-bti-3': [0, 0],
    # 'q5b-bit-3': [0, 0],
    #
    # 'q1-ni-2': [1.231017793599974, 9.585686507874938],
    # 'q1-ni-1': [1.4004054172636395, 10.925616687561162],
}


if __name__ == '__main__':
    plt.rc('text', usetex=True), plt.rc('font', family='serif', size=20)

    # First, let's just plot all queries of Neo4J against Cassandra.
    plt.figure()
    plt.subplot(121)
    k = iter(['C0', 'C1', 'C1', 'C2', 'C3', 'C3', 'C4'])
    for i, q in enumerate(sorted([x for x in c if 'ni' in x and '-3' in x])):
        plt.bar([1 + 0.2 * i], [c[q][0]], 0.2, color=[k.__next__()])
    plt.xlabel('Cassandra'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002), plt.ylabel('Running Time (s)')
    plt.gca().set_ylim([0, 12])
    plt.xticks([]), plt.subplot(122)

    k = iter(['C0', 'C1', 'C1', 'C2', 'C2', 'C3', 'C3', 'C4', 'C4'])
    for i, q in enumerate(sorted([y for y in n if 'ni' in y and '-3' in y])):
        plt.bar([1 + 0.2 * i], [n[q][0]], 0.2, color=[k.__next__()])
    plt.xlabel('Neo4J'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002)
    plt.xticks([]), plt.yticks([])
    plt.gca().set_ylim([0, 12])
    plt.subplots_adjust(wspace=0.0, left=0.16, right=0.98, bottom=0.12, top=0.97), plt.show()

    # Next, let's plot queries 1, 3, and 5 with and without an index on TYC1.
    plt.figure()
    plt.subplot(131)
    for i, q in enumerate([c['q1-ni-3'], c['q3-ni-3'], c['q5-ni-3']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel('Cassandra'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002), plt.ylabel('Running Time (s)')
    plt.gca().set_ylim([0, 12]), plt.xticks([]), plt.subplot(132)

    for i, q in enumerate([n['q1-ni-3'], n['q3a-ni-3'], n['q5a-ni-3']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel(r'\ Neo4J \\ (No Index)'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002)
    plt.gca().set_ylim([0, 12]), plt.yticks([]), plt.xticks([]), plt.subplot(133)

    for i, q in enumerate([n['q1-tyc1i-3'], n['q3a-tyc1i-3'], n['q5a-tyc1i-3']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel(r'\ \ Neo4J \\ (TYC1 Index)'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002)
    plt.gca().set_ylim([0, 12]), plt.yticks([]), plt.xticks([])
    plt.subplots_adjust(wspace=0.0, left=0.16, right=0.98, bottom=0.12, top=0.97), plt.show()

    # Next, let's plot queries 4 and 5 with and without an index on BTmag.
    plt.figure()
    plt.subplot(121)
    for i, q in enumerate([c['q4a-ni-3'], c['q5-ni-3'], c['q4a-bti-3'], c['q5-bti-3']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel('Cassandra'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002), plt.ylabel('Running Time (s)')
    plt.gca().set_ylim([0, 12]), plt.xticks([]), plt.subplot(122)

    for i, q in enumerate([n['q4a-ni-3'], n['q5a-ni-3'], n['q4a-bti-3'], n['q5a-bti-3']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel('Neo4J'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002)
    plt.gca().set_ylim([0, 12]), plt.xticks([]), plt.yticks([])
    plt.subplots_adjust(wspace=0.0, left=0.16, right=0.98, bottom=0.12, top=0.97), plt.show()

    # Finally, let us plot query 1 for clusters of different size.
    plt.figure()
    plt.subplot(131)
    for i, q in enumerate([c['q1-ni-1'], n['q1-ni-1']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel('1 Node'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002), plt.ylabel('Running Time (s)')
    plt.gca().set_ylim([0, 12]), plt.xticks([]), plt.subplot(132)

    for i, q in enumerate([c['q1-ni-2'], n['q1-ni-2']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel('2 Nodes'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002)
    plt.gca().set_ylim([0, 12]), plt.xticks([]), plt.yticks([]), plt.subplot(133)

    for i, q in enumerate([c['q1-ni-3'], n['q1-ni-3']]):
        plt.bar([1 + 0.2 * i], q[0], 0.2)
    plt.xlabel('3 Nodes'), plt.yscale('symlog', nonposy='clip', linthreshy=0.002)
    plt.gca().set_ylim([0, 12]), plt.xticks([]), plt.yticks([])
    plt.subplots_adjust(wspace=0.0, left=0.16, right=0.98, bottom=0.12, top=0.97), plt.show()


