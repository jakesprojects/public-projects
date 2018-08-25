def adjust_hex(hex_str,amount=-.5):
    hex_str = hex_str.replace('#','',1)
    components = []
    for i in range(0,6,2):
        component = hex_str[i:][:2]
        component = eval('0x'+component)
        component = (1-amount)*component
        component = int(round(component,0))
        component = max([min([component,255]),0])
        component = hex(component).replace('0x','',1)
        component = component.upper()
        component = '{:0>2}'.format(component)
        components.append(component)
    return '#'+''.join(components)
