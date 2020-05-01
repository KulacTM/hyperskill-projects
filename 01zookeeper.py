<html>
<head>
<title>zookeeper.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #a9b7c6;}
.s1 { color: #6a8759;}
.s2 { color: #cc7832;}
.s3 { color: #6897bb;}
.s4 { color: #808080;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
zookeeper.py</font>
</center></td></tr></table>
<pre><span class="s0">camel = </span><span class="s1">&quot;&quot;&quot; 
Switching on camera from habitat with camels... 
 ___.-''''-. 
/___  @    | 
',,,,.     |         _.'''''''._ 
     '     |        /           </span><span class="s2">\\</span>
     <span class="s1">|     \    _.-'             </span><span class="s2">\\</span>
     <span class="s1">|      '.-'                  '-. 
     |                               ', 
     |                                '', 
      ',,-,                           ':; 
           ',,| ;,,                 ,' ;; 
              ! ; !'',,,',',,,,'!  ;   ;: 
             : ;  ! !       ! ! ;  ;   :; 
             ; ;   ! !      ! !  ; ;   ;, 
            ; ;    ! !     ! !   ; ;      
            ; ;    ! !    ! !     ; ; 
           ;,,      !,!   !,!     ;,; 
           /_I      L_I   L_I     /_I 
Yey, our little camel is sunbathing!&quot;&quot;&quot;</span>

<span class="s0">lion = </span><span class="s1">&quot;&quot;&quot; 
Switching on camera from habitat with lions... 
                                               ,w. 
                                             ,YWMMw  ,M  , 
                        _.---.._   __..---._.'MMMMMw,wMWmW, 
                   _.-&quot;&quot;        '''           YP&quot;WMMMMMMMMMb, 
                .-' __.'                   .'     MMMMW^WMMMM; 
    _,        .'.-'&quot;; `,       /`     .--&quot;&quot;      :MMM[==MWMW^; 
 ,mM^&quot;     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW&quot;  @</span><span class="s2">\\</span>
<span class="s1">,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `&quot;=./`-, 
WMMm__,-'.'     /      _.\      F'''-+,,   ;_,_.dMMMMMMMM[,_ / `=_} 
&quot;^MP__.-'    ,-' _.--&quot;&quot;   `-,   ;       \  ; ;MMMMMMMMMMW^``; __| 
           /   .'            ; ;         )  )`{  \ `&quot;^W^`,   \  : 
          /  .'             /  (       .'  /     Ww._     `.  `&quot; 
         /  Y,              `,  `-,=,_{   ;      MMMP`&quot;&quot;-,  `-._.-, 
        (--, )                `,_ / `) \/&quot;&quot;)      ^&quot;      `-, -;&quot;\:</span>
<span class="s1">The lion is croaking!&quot;&quot;&quot;</span>

<span class="s0">deer = </span><span class="s1">&quot;&quot;&quot; 
Switching on camera from habitat with deers... 
   /|       |</span><span class="s2">\\</span>
<span class="s1">`__</span><span class="s2">\\\\       </span><span class="s1">//__' 
   ||      || 
 \__`\     |'__/ 
   `_</span><span class="s2">\\\\   </span><span class="s1">//_' 
   _.,:---;,._ 
   \_:     :_/ 
     |@. .@| 
     |     | 
     ,\.-./ </span><span class="s2">\\</span>
     <span class="s1">;;`-'   `---__________-----.-. 
     ;;;                         \_</span><span class="s2">\\</span>
     <span class="s1">';;;                         | 
      ;    |                      ; 
       \   \     \        |      / 
        \_, \    /        \     |</span><span class="s2">\\</span>
          <span class="s1">|';|  |,,,,,,,,/ \    \ \_</span>
          <span class="s1">|  |  |           \   /   | 
          \  \  |           |  / \  | 
           | || |           | |   | | 
           | || |           | |   | | 
           | || |           | |   | | 
           |_||_|           |_|   |_| 
          /_//_/           /_/   /_/ 
Our 'Bambi' looks hungry. Let's go to feed it!&quot;&quot;&quot;</span>

<span class="s0">goose = </span><span class="s1">&quot;&quot;&quot; 
Switching on camera from habitat with lovely goose... 
 
                                    _ 
                                ,-&quot;&quot; &quot;&quot;. 
                              ,'  ____  `. 
                            ,'  ,'    `.  `._ 
   (`.         _..--.._   ,'  ,'        \    </span><span class="s2">\\</span>
  <span class="s1">(`-.\    .-&quot;&quot;        &quot;&quot;'   /          (  d _b 
 (`._  `-&quot;&quot; ,._             (            `-(   </span><span class="s2">\\</span>
 <span class="s1">&lt;_  `     (  &lt;`&lt;            \              `-._</span><span class="s2">\\</span>
  <span class="s1">&lt;`-       (__&lt; &lt;           : 
   (__        (_&lt;_&lt;          ; 
    `------------------------------------------ 
This bird stares intently at you... (Maybe it's time to change the channel?)&quot;&quot;&quot;</span>

<span class="s0">bat = </span><span class="s1">&quot;&quot;&quot; 
Switching on camera from habitat with bats... 
_________________               _________________ 
 ~-.              \  |\___/|  /              .-~ 
     ~-.           \ / o o \ /           .-~ 
        &gt;           </span><span class="s2">\\\\  </span><span class="s1">W  //           &lt; 
       /             /~---~\             </span><span class="s2">\\</span>
      <span class="s1">/_            |       |            _</span><span class="s2">\\</span>
         <span class="s1">~-.        |       |        .-~ 
            ;        \     /        i 
           /___      /\   /\      ___</span><span class="s2">\\</span>
                <span class="s1">~-. /  \_/  \ .-~ 
                   V         V 
It looks like this bat is fine.&quot;&quot;&quot;</span>

<span class="s0">rabbit = </span><span class="s1">&quot;&quot;&quot; 
Switching on camera from habitat with rabbits... 
         , 
        /|      __ 
       / |   ,-~ / 
      Y :|  //  / 
      | jj /( .^ 
      &gt;-&quot;~&quot;-v&quot; 
     /       Y 
    jo  o    | 
   ( ~T~     j 
    &gt;._-' _./ 
   /   &quot;~&quot;  | 
  Y     _,  | 
 /| ;-&quot;~ _  l 
/ l/ ,-&quot;~    </span><span class="s2">\\</span>
<span class="s1">\//\/      .- </span><span class="s2">\\</span>
 <span class="s1">Y        /    Y  
 l       I     ! 
 ]\      _\    /&quot;</span><span class="s2">\\</span>
<span class="s1">(&quot; ~----( ~   Y.  ) 
It seems there will be more rabbits soon!&quot;&quot;&quot;</span>

<span class="s0">animals = [camel</span><span class="s2">, </span><span class="s0">lion</span><span class="s2">, </span><span class="s0">deer</span><span class="s2">, </span><span class="s0">goose</span><span class="s2">, </span><span class="s0">bat</span><span class="s2">, </span><span class="s0">rabbit]</span>
<span class="s2">while True</span><span class="s0">:</span>
    <span class="s0">print(</span><span class="s1">&quot;Which habitat # do you need?&quot;</span><span class="s0">)</span>
    <span class="s0">animal_number = input()</span>
    <span class="s2">if </span><span class="s0">str(animal_number) == </span><span class="s1">'exit'</span><span class="s0">:</span>
        <span class="s0">print(</span><span class="s1">&quot;See you!&quot;</span><span class="s0">)</span>
        <span class="s2">break</span>
    <span class="s2">if </span><span class="s0">int(animal_number) == </span><span class="s3">0</span><span class="s0">:</span>
        <span class="s0">print(camel)</span>
    <span class="s2">if </span><span class="s0">int(animal_number) == </span><span class="s3">1</span><span class="s0">:</span>
        <span class="s0">print(lion)</span>
    <span class="s2">if </span><span class="s0">int(animal_number) == </span><span class="s3">2</span><span class="s0">:</span>
        <span class="s0">print(deer)</span>
    <span class="s2">if </span><span class="s0">int(animal_number) == </span><span class="s3">3</span><span class="s0">:</span>
        <span class="s0">print(goose)</span>
    <span class="s2">if </span><span class="s0">int(animal_number) == </span><span class="s3">4</span><span class="s0">:</span>
        <span class="s0">print(bat)</span>
    <span class="s2">if </span><span class="s0">int(animal_number) == </span><span class="s3">5</span><span class="s0">:</span>
        <span class="s0">print(rabbit)</span>

<span class="s4"># write your code here</span>
</pre>
</body>
</html>