# pyRTS
start the example with test_4x4.py or hello_world_lightrts.py
## states
![image](https://user-images.githubusercontent.com/66048062/228518275-96ddbe40-1d35-44ee-914f-fc0a9cbe329f.png)
red:player1, bule: player2, circle: worker, green square: resource, green triangle: direction 


shape = (num_envs,map_height*map_width,grid_state)

gird_state
<table class="MsoNormalTable" border="1" cellspacing="0" cellpadding="0" width="264" style="width:198.2pt;border-collapse:collapse;border:none;mso-border-alt:solid windowtext .5pt;
 mso-yfti-tbllook:1184;mso-padding-alt:0cm 5.4pt 0cm 5.4pt;mso-border-insideh:
 .5pt solid windowtext;mso-border-insidev:.5pt solid windowtext">
 <tbody><tr style="mso-yfti-irow:0;mso-yfti-firstrow:yes;height:14.0pt">
  <td width="104" nowrap="" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">name<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">type<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border:solid windowtext 1.0pt;
  border-left:none;mso-border-left-alt:solid windowtext .5pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">default<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:1;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">PLAYER1<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:2;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">PLAYER2<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:3;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">NONE<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:4;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">WAITING<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">int<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:5;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">WORKER<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:6;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">SOLDIER<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:7;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">BASE<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:8;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">BARRACKS<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:9;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">RESOURCE<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:10;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">HP<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">int<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:11;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ATK<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">int<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:12;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ATKRANGE<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">int<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:13;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">RP<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">int<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:14;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">MOVING<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:15;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ATTACKING<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:16;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">HARVESTING<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:17;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">RETURNING<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:18;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">PRODUCING<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:19;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ACTIONUP<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:20;height:17.5pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:17.5pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ACTIONRIGHT<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:17.5pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:17.5pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:21;height:13.55pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:13.55pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ACTIONDOWN<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:13.55pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:13.55pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:22;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">ACTIONLEFT<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">bool<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">0<o:p></o:p></span></p>
  </td>
 </tr>
 <tr style="mso-yfti-irow:23;mso-yfti-lastrow:yes;height:14.0pt">
  <td width="104" valign="top" style="width:78.0pt;border:solid windowtext 1.0pt;
  border-top:none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:8.0pt;font-family:&quot;Segoe UI&quot;,sans-serif;
  mso-fareast-font-family:等线;color:#1F2328;mso-font-kerning:0pt">TARGET<o:p></o:p></span></p>
  </td>
  <td width="66" nowrap="" valign="bottom" style="width:49.35pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="left" style="text-align:left;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">int<o:p></o:p></span></p>
  </td>
  <td width="94" nowrap="" valign="bottom" style="width:70.85pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-left-alt:solid windowtext .5pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:14.0pt">
  <p class="MsoNormal" align="right" style="text-align:right;mso-pagination:widow-orphan"><span lang="EN-US" style="font-size:11.0pt;mso-ascii-font-family:等线;mso-fareast-font-family:
  等线;mso-hansi-font-family:等线;mso-bidi-font-family:宋体;color:black;mso-font-kerning:
  0pt">-1<o:p></o:p></span></p>
  </td>
 </tr>
</tbody></table>


