from divewidgets import create_flowchart


sort_two_values_fc1 = create_flowchart(code=r"""
st=>start: Start
cond1=>condition: if (x <= y)
cond2=>condition: if (y < x)
suite1=>inputoutput: print(x, y)
suite2=>inputoutput: print(y, x)
e=>end

st(right)->cond1
cond1(yes)->suite1(right)->cond2
cond1(no, right)->cond2
cond2(yes)->suite2(right)->e
cond2(no)->e
""")

sort_two_values_fc2 = create_flowchart(code=r"""
st=>start: Start
cond1=>condition: if (x <= y)
suite1=>inputoutput: print(x, y)
suite2=>inputoutput: print(y, x)
e=>end

st(right)->cond1
cond1(yes)->suite1(right)->e
cond1(no)->suite2(bottom)->e
""")

sort_three_values_fc = create_flowchart(code=r"""
st=>start: Start
cond1=>condition: if (x <= y <= z)
suite1=>inputoutput: print(x, y, z)
cond2=>condition: if (x <= z <= y)
suite2=>inputoutput: print(x, z, y)
cond3=>condition: if (y <= x <= z)
suite3=>inputoutput: print(y, x, z)
cond4=>condition: if (y <= z <= x)
suite4=>inputoutput: print(y, z, x)
cond5=>condition: if (z <= x <= y)
suite5=>inputoutput: print(z, x, y)
suite6=>inputoutput: print(z, y, x)

e=>end

st->cond1
cond1(yes)->suite1->e
cond1(no)->cond2
cond2(yes)->suite2->e
cond2(no)->cond3
cond3(yes)->suite3->e
cond3(no)->cond4
cond4(yes)->suite4->e
cond4(no)->cond5
cond5(yes)->suite5->e
cond5(no)->suite6->e
""")