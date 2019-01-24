import reportgen as rpt
import pandas as pd
# Open a pptx file
p=rpt.Report('template.pptx')# The parameters can be defaulted
# add a cover
p.add_cover(title='A analysis report powered by reportgen')
# add a chart slide
data=pd.DataFrame({'Jack':[90,80,100],'David':[100,70,85]},index=['Math','English','Physics'])
p.add_slide(data={'data':data,'slide_type':'chart','type':'COLUMN_CLUSTERED'},\
title='the scores report',summary='Our class got excellent results',footnote='This is a footnote.')
# add a table slide
data=pd.DataFrame({'Jack':[90,80,100],'David':[100,70,85]},index=['Math','English','Physics'])
p.add_slide(data={'data':data,'slide_type':'table'},title='the scores report',summary='Our class got excellent results',footnote='This is a footnote.')
# add a textbox slide
data='This a paragraph. \n'*4
p.add_slide(data={'data':data,'slide_type':'textbox'},title='This is a textbox slide',summary='',footnote='')
# add a picture slide
data='.\\images\\logo.png'
p.add_slide(data={'data':data,'slide_type':'picture'},title='This is a picture slide')
p.save('analysis report.pptx')