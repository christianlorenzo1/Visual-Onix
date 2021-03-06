
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '75D2D0FBE0C8D3DE7083F388DAD590C0'
    
_lr_action_items = {'CREATEHTML':([0,],[1,]),'CIRCLE':([0,],[2,]),'STRINGVALUE':([8,29,],[-14,35,]),'POLYGON':([0,],[4,]),'END':([0,],[5,]),'LINE':([0,],[6,]),'RECT':([0,],[9,]),'ID':([0,8,23,24,30,31,33,34,37,39,40,47,49,52,54,57,59,62,64,67,69,72,73,],[8,-14,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'COLON':([14,32,45,48,53,58,63,68,],[20,38,46,50,55,60,65,70,]),'TEXT':([0,],[11,]),'NUMBER':([2,3,4,6,9,11,12,13,15,16,17,18,19,20,21,22,25,26,27,28,38,42,46,47,50,52,55,57,60,62,65,67,70,],[12,13,14,15,16,17,18,19,21,22,23,24,25,26,27,28,31,32,33,34,42,45,47,48,52,53,57,58,62,63,67,68,72,]),'$end':([1,5,7,8,10,35,36,41,43,44,51,56,61,66,71,74,],[-1,-13,0,-14,-15,-12,-2,-4,-5,-3,-6,-7,-8,-9,-10,-11,]),'ELLIPSE':([0,],[3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,],[7,]),'term':([0,23,24,30,31,33,34,37,39,40,47,49,52,54,57,59,62,64,67,69,72,73,],[10,29,30,36,37,39,40,41,43,44,49,51,54,56,59,61,64,66,69,71,73,74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> CREATEHTML','expression',1,'p_expression_createhtml','Parser.py',18),
  ('expression -> CIRCLE NUMBER NUMBER NUMBER term term','expression',6,'p_expression_circle','Parser.py',25),
  ('expression -> RECT NUMBER NUMBER NUMBER NUMBER term term','expression',7,'p_expression_rectangle','Parser.py',32),
  ('expression -> ELLIPSE NUMBER NUMBER NUMBER NUMBER term term','expression',7,'p_expression_ellipse','Parser.py',38),
  ('expression -> LINE NUMBER NUMBER NUMBER NUMBER term term','expression',7,'p_expression_line','Parser.py',44),
  ('expression -> POLYGON NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER term term','expression',12,'p_expression_polygon','Parser.py',50),
  ('expression -> POLYGON NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER term term','expression',15,'p_expression_polygon','Parser.py',51),
  ('expression -> POLYGON NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER term term','expression',18,'p_expression_polygon','Parser.py',52),
  ('expression -> POLYGON NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER term term','expression',21,'p_expression_polygon','Parser.py',53),
  ('expression -> POLYGON NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER term term','expression',24,'p_expression_polygon','Parser.py',54),
  ('expression -> POLYGON NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER NUMBER COLON NUMBER term term','expression',27,'p_expression_polygon','Parser.py',55),
  ('expression -> TEXT NUMBER NUMBER term STRINGVALUE','expression',5,'p_expression_text','Parser.py',71),
  ('expression -> END','expression',1,'p_expression_end','Parser.py',77),
  ('term -> ID','term',1,'p_term_ID','Parser.py',88),
  ('expression -> term','expression',1,'p_expression_term','Parser.py',96),
]
