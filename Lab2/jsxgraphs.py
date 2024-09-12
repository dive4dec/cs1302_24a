from divewidgets import create_JSXGraph

pythagorean1 = create_JSXGraph(code=r"""
JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-1, 15, 17, -3], axis:true, grid:true, showCopyright:false});
var a = board.create('slider', [[1, -1], [5,-1], [2, 4, 7]], {name:'a', snapWidth: 0.1});
var b = board.create('slider', [[8, -1], [12,-1], [2, 3, 7]], {name:'b', snapWidth: 0.1});

var s = board.create('point', [6,6],{face:"", withLabel:false});
var right_ab = board.create('transform', [()=>a.Value()+b.Value(),0], {type:'translate'});
var right_a = board.create('transform', [()=>a.Value(),0], {type:'translate'});
var right_b = board.create('transform', [()=>b.Value(),0], {type:'translate'});
var left_a = board.create('transform', [()=> -a.Value(),0], {type:'translate'});
var left_b = board.create('transform', [()=> -b.Value(),0], {type:'translate'});
var up_ab = board.create('transform', [0,()=>a.Value()+b.Value()], {type:'translate'});
var up_a = board.create('transform', [0,()=>a.Value()], {type:'translate'});
var up_b = board.create('transform', [0,()=>b.Value()], {type:'translate'});
var down_a = board.create('transform', [0,()=> -a.Value()], {type:'translate'});
var down_b = board.create('transform', [0,()=> -b.Value()], {type:'translate'});
var no_move = board.create('transform', [0,0], {type:'translate'});


var tri1 = [];
tri1[0] = board.create('point', [s, up_b], {visible: true, size:2, name:'A', label:{offset:[-10,10]}});
tri1[1] = board.create('point', [tri1[0], down_b], {visible: true, size:2, name:'C', label:{offset:[-10,-10]}});
tri1[2] = board.create('point', [tri1[0], [down_b,right_a]], {visible: true, size:2, name:'B', label:{offset:[10,0]}});
var po1 = board.create('polygon',[tri1[0], tri1[1],tri1[2]], 
                        {withLines: true, fillColor:'none', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('segment',[tri1[0],tri1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[-10, b.Value()/2]}});
board.create('segment',[tri1[1],tri1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a.Value()/2, -10]}});
board.create('segment',[tri1[2],tri1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a.Value()/2-10, b.Value()/2-10]}});


var po_a = board.create('regularpolygon',[tri1[1],tri1[0],4], 
                        {withLines: true, fillColor:'red', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var po_b = board.create('regularpolygon',[tri1[2],tri1[1],4], 
                        {withLines: true, fillColor:'green', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var po_c = board.create('regularpolygon',[tri1[0],tri1[2],4], 
                        {withLines: true, fillColor:'yellow', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});


board.create('text',[()=>s.X()+a.Value()/2,()=>s.Y()-a.Value()/2,function(){
        return (po_b.Area()).toFixed(2);
    }],{anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()-b.Value()/2,()=>s.Y()+b.Value()/2,function(){
        return (po_a.Area()).toFixed(2);
    }],{anchorX: 'middle', anchorY: 'auto'});
    
board.create('text',[()=>s.X()+a.Value(),()=>s.Y()+b.Value(),function(){
        return (po_c.Area()).toFixed(2);
    }],{anchorX: 'middle', anchorY: 'auto'});
""")

pythagorean2 = create_JSXGraph(code=r"""
JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-1, 13, 15, -3], axis:true, showCopyright:false});
var a = board.create('slider', [[1, -1], [5,-1], [2, 6, 7]], {name:'a', snapWidth: 0.1});
var b = board.create('slider', [[8, -1], [12,-1], [2, 3, 7]], {name:'b', snapWidth: 0.1});
var m = board.create('slider', [[1, -2], [12,-2], [0, 0, 2]], {name:'move', snapWidth: 0.1, withLabel:false});
board.create('text',[1+m.point2.X(),m.point2.Y(),"move"],{fixed: true, anchorX: 'middle'});
var s = board.create('point', [1,1],{face:"", withLabel:false});
var right_ab = board.create('transform', [()=>a.Value()+b.Value(),0], {type:'translate'});
var right_a = board.create('transform', [()=>a.Value(),0], {type:'translate'});
var right_b = board.create('transform', [()=>b.Value(),0], {type:'translate'});
var left_a = board.create('transform', [()=> -a.Value(),0], {type:'translate'});
var left_b = board.create('transform', [()=> -b.Value(),0], {type:'translate'});
var up_ab = board.create('transform', [0,()=>a.Value()+b.Value()], {type:'translate'});
var up_a = board.create('transform', [0,()=>a.Value()], {type:'translate'});
var up_b = board.create('transform', [0,()=>b.Value()], {type:'translate'});
var down_a = board.create('transform', [0,()=> -a.Value()], {type:'translate'});
var down_b = board.create('transform', [0,()=> -b.Value()], {type:'translate'});
var no_move = board.create('transform', [0,0], {type:'translate'});


var r2 = board.create('point', [s,right_ab], {visible: false});
var po0 =  board.create('regularpolygon',[s,r2,4], 
                        {withLines: true, fillColor:'none', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var tri1 = [];
tri1[0] = board.create('point', [s, up_b], {visible: false});
tri1[1] = board.create('point', [tri1[0], down_b], {visible: false});
tri1[2] = board.create('point', [tri1[0], [down_b,right_a]], {visible: false});
var po1 = board.create('polygon',[tri1[0],tri1[1],tri1[2]], 
                        {withLines: true, fillColor:'red', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('segment',[tri1[0],tri1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[-10, b.Value()/2]}});
board.create('segment',[tri1[1],tri1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a.Value()/2, -10]}});
board.create('segment',[tri1[2],tri1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a.Value()/2-10, b.Value()/2-10]}});

var move_tri2 = board.create('transform', [()=>a.Value(), ()=>b.Value()*(1-Math.min(m.Value(),1))], {type:'translate'});
var tri2 = [];
tri2[0] = board.create('point', [s, move_tri2], {visible: false});
tri2[1] = board.create('point', [tri2[0], right_b], {visible: false});
tri2[2] = board.create('point', [tri2[0], [right_b,up_a]], {visible: false});
var po2 = board.create('polygon',[tri2[0],tri2[1],tri2[2]], 
                        {withLines: true, fillColor:'green', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var move_tri3 = board.create('transform', [()=>a.Value()+b.Value()*(Math.max(m.Value(),1)-1), ()=>a.Value()*(Math.max(m.Value(),1)-1)], {type:'translate'});
var tri3 = [];
tri3[0] = board.create('point', [s, move_tri3], {visible: false});
tri3[1] = board.create('point', [tri3[0], up_b], {visible: false});
tri3[2] = board.create('point', [tri3[0], [up_b,left_a]], {visible: false});
var po3 = board.create('polygon',[tri3[0],tri3[1],tri3[2]], 
                        {withLines: true, fillColor:'blue', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});


var move_tri4 = board.create('transform', [()=>b.Value()+a.Value()*(1-Math.min(m.Value(),1)), ()=>a.Value()+b.Value()], {type:'translate'});
var tri4 = [];
tri4[0] = board.create('point', [s, move_tri4], {visible: false});
tri4[1] = board.create('point', [tri4[0], left_b], {visible: false});
tri4[2] = board.create('point', [tri4[0], [left_b,down_a]], {visible: false});
var po4 = board.create('polygon',[tri4[0],tri4[1],tri4[2]], 
                        {withLines: true, fillColor:'yellow', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('text',[()=>s.X()+1/2*a.Value(),()=>s.Y()+b.Value()+1/2*a.Value(),function(){
        return '\\[ a^2 \\]';
    }],{visible: ()=> {return (m.Value()<0.3);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+a.Value()+1/2*b.Value(),()=>s.Y()+1/2*b.Value(),function(){
    return '\\[b^2\\]';
    }],{visible: ()=> {return (m.Value()<0.3);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+1/2*(a.Value()+b.Value()),()=>s.Y()+1/2*(a.Value()+b.Value()),function(){
    return '\\[c^2\\]';
    }],{visible: ()=> {return (m.Value()>1.9);}, anchorX: 'middle', anchorY: 'auto'});
""")

pythagorean3 = create_JSXGraph(code=r"""
JXG.Options.text.useMathJax = true;
var board = JXG.JSXGraph.initBoard('box', {boundingbox: [-1, 13, 15, -3], axis:true, showCopyright:false});
var a = board.create('slider', [[1, -1], [5,-1], [2, 6, 7]], {name:'a', snapWidth: 0.1});
var b = board.create('slider', [[8, -1], [12,-1], [2, 3, 7]], {name:'b', snapWidth: 0.1});
var m = board.create('slider', [[1, -2], [12,-2], [0, 0, 2]], {name:'move', snapWidth: 0.1, withLabel:false});
board.create('text',[1+m.point2.X(),m.point2.Y(),"move"],{fixed: true, anchorX: 'middle'});
var s = board.create('point', [1,1],{face:"", withLabel:false});
var right_ab = board.create('transform', [()=>a.Value()+b.Value(),0], {type:'translate'});
var right_a = board.create('transform', [()=>a.Value(),0], {type:'translate'});
var right_b = board.create('transform', [()=>b.Value(),0], {type:'translate'});
var left_a = board.create('transform', [()=> -a.Value(),0], {type:'translate'});
var left_b = board.create('transform', [()=> -b.Value(),0], {type:'translate'});
var up_ab = board.create('transform', [0,()=>a.Value()+b.Value()], {type:'translate'});
var up_a = board.create('transform', [0,()=>a.Value()], {type:'translate'});
var up_b = board.create('transform', [0,()=>b.Value()], {type:'translate'});
var down_a = board.create('transform', [0,()=> -a.Value()], {type:'translate'});
var down_b = board.create('transform', [0,()=> -b.Value()], {type:'translate'});
var no_move = board.create('transform', [0,0], {type:'translate'});


var r2 = board.create('point', [s,right_ab], {visible: false});
var po0 =  board.create('regularpolygon',[s,r2,4], 
                        {withLines: true, fillColor:'none', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var tri1 = [];
tri1[0] = board.create('point', [s, up_b], {visible: false});
tri1[1] = board.create('point', [tri1[0], down_b], {visible: false});
tri1[2] = board.create('point', [tri1[0], [down_b,right_a]], {visible: false});
var po1 = board.create('polygon',[tri1[0],tri1[1],tri1[2]], 
                        {withLines: true, fillColor:'red', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

board.create('segment',[tri1[0],tri1[1]],{strokeWidth:0, withLabel: true, name:'b', label:{offset:[-10, b.Value()/2]}});
board.create('segment',[tri1[1],tri1[2]],{strokeWidth:0, withLabel: true, name:'a', label:{offset:[a.Value()/2, -10]}});
board.create('segment',[tri1[2],tri1[0]],{strokeWidth:0, withLabel: true, name:'c', label:{offset:[a.Value()/2-10, b.Value()/2-10]}});

var move_tri2 = board.create('transform', [()=>a.Value(), 0], {type:'translate'});
var tri2 = [];
tri2[0] = board.create('point', [s, move_tri2], {visible: false});
tri2[1] = board.create('point', [tri2[0], right_b], {visible: false});
tri2[2] = board.create('point', [tri2[0], [right_b,up_a]], {visible: false});
var po2 = board.create('polygon',[tri2[0],tri2[1],tri2[2]], 
                        {withLines: true, fillColor:'green', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

//anchor of tri3 should be changed
/*
var move_tri3 = board.create('transform', [()=>a.Value()+b.Value(), ()=>a.Value()], {type:'translate'});
var tri3 = [];
tri3[0] = board.create('point', [s, move_tri3], {visible: false});
tri3[1] = board.create('point', [tri3[0], up_b], {visible: false});
tri3[2] = board.create('point', [tri3[0], [up_b,left_a]], {visible: false});
var po3 = board.create('polygon',[tri3[0],tri3[1],tri3[2]], 
                        {withLines: true, fillColor:'blue', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});
*/

var move_tri3_2 = board.create('transform', [()=>b.Value(), ()=>a.Value()+b.Value()], {type:'translate'});
var tri3_2 = [];
tri3_2[0] = board.create('point', [s, move_tri3_2], {visible: false});
tri3_2[1] = board.create('point', [tri3_2[0], right_a], {visible: false});
tri3_2[2] = board.create('point', [tri3_2[0], [right_a, down_b]], {visible: false});
var po3 = board.create('polygon',[tri3_2[0],tri3_2[1],tri3_2[2]], 
                        {withLines: true, fillColor:'blue', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var move_tri4 = board.create('transform', [()=>b.Value(), ()=>a.Value()+b.Value()], {type:'translate'});
var tri4 = [];
tri4[0] = board.create('point', [s, move_tri4], {visible: false});
tri4[1] = board.create('point', [tri4[0], left_b], {visible: false});
tri4[2] = board.create('point', [tri4[0], [left_b,down_a]], {visible: false});
var po4 = board.create('polygon',[tri4[0],tri4[1],tri4[2]], 
                        {withLines: true, fillColor:'yellow', highlightFillColor:'none',
                         vertices:{face:'', withLabel: false},
                         borders: {strokeWidth:1, strokeColor:'black'}});

var rot_tri2 = board.create('transform', [function(){return m.Value()*Math.PI/4;}, tri2[0]], {type:'rotate'});
rot_tri2.bindTo([tri2[1],tri2[2]]);

var rot_tri3 = board.create('transform', [function(){return - m.Value()*Math.PI/4;}, tri3_2[0]], {type:'rotate'});
rot_tri3.bindTo([tri3_2[1],tri3_2[2]]);

board.create('segment',[tri2[1], board.create('point', [tri2[1], right_b], {visible: false})],{visible:()=>(m.Value()>=1.99),strokeWidth:1, dash:2});


board.create('text',[()=>s.X()+a.Value()*1/2+b.Value(),()=>s.Y()+b.Value()+1/2*a.Value(),function(){
        return '\\[ a^2 \\]';
    }],{visible: ()=> {return (m.Value()>=1.99);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+a.Value()+1/2*b.Value(),()=>s.Y()+1/2*b.Value(),function(){
    return '\\[b^2\\]';
    }],{visible: ()=> {return (m.Value()>=1.99);}, anchorX: 'middle', anchorY: 'auto'});

board.create('text',[()=>s.X()+1/2*(a.Value()+b.Value()),()=>s.Y()+1/2*(a.Value()+b.Value()),function(){
    return '\\[c^2\\]';
    }],{visible: ()=> {return (m.Value()<0.4);}, anchorX: 'middle', anchorY: 'auto'});
""")

parabola = create_JSXGraph(code=r"""
JXG.Options.text.useMathJax = true;
var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-8, 8, 8, -8], axis:true,  showCopyright:false});
var a = brd.create('slider', [[3, -3], [6,-3], [-3, 1, 3]], {name:'a', snapWidth: 0.1});
var b = brd.create('slider', [[3, -4], [6,-4], [-3, 0, 3]], {name:'b', snapWidth: 0.1});
var c = brd.create('slider', [[3, -5], [6,-5], [-3, 0, 3]], {name:'c', snapWidth: 0.1});
var graph1 = brd.create('functiongraph', [function(x){return a.Value()*x*x + b.Value()*x + c.Value();}, -10, 10]);
var text1 = brd.create('text',[-6,2,function(){return '\\[y=ax^2+bx+c\\]';}]);
""")

quadratic = create_JSXGraph(code=r"""
JXG.Options.text.useMathJax = true;
var brd = JXG.JSXGraph.initBoard('box', {boundingbox: [-10, 10, 10, -10], axis:true,  showCopyright:false});
var a = brd.create('slider', [[3, -3], [6,-3], [-5, 1, 5]], {name:'a', snapWidth: 0.1});
var b = brd.create('slider', [[3, -4], [6,-4], [-5, 0, 5]], {name:'b', snapWidth: 0.1});
var c = brd.create('slider', [[3, -5], [6,-5], [-5, 0, 5]], {name:'c', snapWidth: 0.1});
var graph1 = brd.create('functiongraph', [function(x){return a.Value()*x*x + b.Value()*x + c.Value();}, -10, 10]);
var line1 = brd.create('line',[[-10,0],[10,0]], {visible: false});
var inter1 = brd.create('intersection',[graph1, line1, 0],{name:"\\[x_1\\]"});
var inter2 = brd.create('intersection',[graph1, line1, 1],{name:"\\[x_2\\]"});
var get_roots = function(a, b, c){
d=Math.sqrt(b*b-4*a*c);

return -b}

var text1 = brd.create('text',[-8,-6,function(){return '\\[y=ax^2+bx+c\\]';}]);
var text2 = brd.create('text',[3,-6,function(){return '\\[b^2-4ac='+(b.Value()*b.Value() - 4*a.Value()*c.Value()).toFixed(2)+'\\]'}])
var text3 = 
""")