import os
import parseConfig as pc
import utils_top_activity as topa

def execCmd(cmd):
    lines = os.popen(cmd)
    text = lines.readlines()
    lines.close()
    return text

def parseComponent(line_text):

    view_object = {}

    pos1 = line_text.find('{')
    pos2 = line_text.find('}')

    view_type = line_text[:pos1].strip()
    view_attr = line_text[pos1+1:pos2].strip()

    #print 'view_type = ', view_type, ', view_attr = ', view_attr
    view_object['view_type'] = view_type

    view_attrs = view_attr.split()
    #print 'view_attrs = ', view_attrs

    view_attr_layout = view_attrs[3]
    layout0 = view_attr_layout.find(',')
    layout1 = view_attr_layout.find('-')
    layout2 = view_attr_layout.rfind(',')

    layout_left = view_attr_layout[:layout0]
    layout_top = view_attr_layout[layout0 + 1: layout1]
    layout_right = view_attr_layout[layout1 + 1: layout2]
    layout_bottom = view_attr_layout[layout2 + 1:]

    #print 'layout: ', layout_left, ', ', layout_top,', ', layout_right,',', layout_bottom
    view_object['view_abs_layout_left'] = int(layout_left)
    view_object['view_abs_layout_top'] = int(layout_top)
    view_object['view_abs_layout_right'] = int(layout_right)
    view_object['view_abs_layout_bottom'] = int(layout_bottom)
    view_object['view_layout_left'] = -1


    if len(view_attrs) > 5:
        view_attr_id = view_attrs[5]
        id_pos = view_attr_id.find('/')
        view_id = view_attr_id[id_pos+1:].strip()
        #print 'viwe_id = ', view_id
        view_object['view_id'] = view_id
    else:
        view_object['view_id'] = ''


    #print 'view_object = ', view_object
    return view_object

    
def getComponent(line_text, view_list, ref_pos):
    
     pos = line_text.find('com.android')
     if(pos == -1):
        pos = line_text.find('android')

     print 'pos = ', pos

     if pos > -1:
        temp = parseComponent(line_text)
        temp['view_level'] = pos - ref_pos - 2 
        view_list.append(temp)

def compute_view_layout(index, view_list):

    index_temp = index -1

    if view_list[index]['view_layout_left']  == -1:
            if view_list[index]['view_level'] == 0:
                view_list[index]['view_layout_left'] = view_list[index]['view_abs_layout_left']
                view_list[index]['view_layout_top'] = view_list[index]['view_abs_layout_top']
                view_list[index]['view_layout_right'] = view_list[index]['view_abs_layout_right']
                view_list[index]['view_layout_bottom'] = view_list[index]['view_abs_layout_bottom']
            else:
                while index_temp > 0 and view_list[index]['view_level'] <= view_list[index_temp]['view_level']:
                    index_temp = index_temp -1

                left, top, right, bottom = compute_view_layout(index_temp,view_list)
                view_list[index]['view_layout_left'] = view_list[index]['view_abs_layout_left'] +  left
                view_list[index]['view_layout_top'] = view_list[index]['view_abs_layout_top'] + top
                view_list[index]['view_layout_right'] = view_list[index]['view_abs_layout_right'] + left
                view_list[index]['view_layout_bottom'] = view_list[index]['view_abs_layout_bottom'] + top



    #print view_list[index]
    return view_list[index]['view_layout_left'], view_list[index]['view_layout_top'],view_list[index]['view_layout_right'],view_list[index]['view_layout_bottom'],


        

def dumpView():
    ref_pos = -1
    view_list = []
    view_index = 0
    package_name = topa.topActivity()
    print 'package_name = ', package_name
    text = execCmd('adb shell dumpsys activity top')

    start_tag = 0
    for aline in text:
        if start_tag == 0:
            ref_pos = aline.find('View Hierarchy')
            if ref_pos > -1:
                start_tag = 1
        else:
            getComponent(aline, view_list, ref_pos)


    #compute real layout
    for i in range(0, len(view_list)):
        compute_view_layout(i, view_list)


    for i in range(0, len(view_list)):
        print 'i = ',i, '-->', view_list[i]
        print '####################################'
    #print 'view_list = ', view_list
    

dumpView()
