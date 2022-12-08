# Naceteni dat z txt soboru a rozdeleni na jednotlive linky kusovniku. Vysledek ulozen jako list.
from inspect import Parameter
from operator import contains
# import openpyxl as excel
import os
from datetime import date


def nacteni_dat(file):
    with open(file) as datafile:
        data = datafile.readlines()
        datafile.close()
    vse_ocistene = []
    for linka in data:
        if linka[0][0] == "|":
            slinka = linka.split("|")
            linka_bez_mezer = []
            for data in slinka:
                data = data.strip()
                data = data.replace(",", "")
                if data == "":
                    data = data.replace("", "0")
                linka_bez_mezer.append(data)
            vse_ocistene.append(linka_bez_mezer)
    return vse_ocistene

# Pro kazdou linku vezme itemy z linky a ulozi jejich hodnoty ex date, lt, ss a routing LT jako dict do listu all parameters.
def databaze_parametru(data, krok):
    all_parameters = {}
    uz_projeto = []
    for line in data:
        i = 0
        item = line[1]
        while item != "0":
            item_parameters = {}            
            if item not in uz_projeto: # Pokud se dil jeste neresil:                
                if item[0:3] != "PMP": # Pro anonymni dil rovnou doplni data.
                    item_parameters["description"] = line[2 + i]               
                    item_parameters["typ"] = line[3 + i]
                    item_parameters["warehouse"] = line[4 + i]
                    item_parameters["exdate"] = line[5 + i]
                    item_parameters["supplytime"] = float(line[6 + i])
                    item_parameters["purchase price"] = float(line[7 + i])
                    item_parameters["purchase currency"] = line[8 + i]
                    item_parameters["purchase price unit"] = line[9 + i]
                    item_parameters["supplier"] = line[10 + i]
                    item_parameters["supplier name"] = line[11 + i]
                    item_parameters["nakupci"] = line[12 + i]
                    item_parameters["ordering system"] = line[13 + i]
                    item_parameters["safetystock"] = float(line[14 + i])
                    item_parameters["sales group"] = line[15 + i]            
                    item_parameters["sales lead time"] = int(line[16 + i])
                    item_parameters["sales price unit"] = line[17 + i]
                    item_parameters["routinglt"] = float(line[18 + i])
                    item_parameters["standardroutinglt"] = float(line[19 + i])
                    item_parameters["phantom"] = line[20 + i]
                    item_parameters["standard cost"] = float(line[21 + i])
                    item_parameters["material cost"] = float(line[22 + i])                
                    item_parameters["operation cost"] = float(line[23 + i])
                    item_parameters["bom qty"] = float(line[24 + i])

                    
                    all_parameters[item] = item_parameters # Prida parametry prave reseneho itemu do parametru vsech itemu z reportu.
                    uz_projeto.append(item) # Prida prave reseny item do seznamu uz projetych itemu.

                    i += krok # Krok na dalsi item v lince. 1/2
                    item = line[1 + i] # Krok na dalsi item v lince. 2/2

                elif item[0:3] == "PMP": # A) Pro projektovy dil rovnou doplni data. B) Vytvori anonymni polozku se stejnymi daty, pokud uz neexistuje.
                    # A)
                    item_parameters["description"] = line[2 + i]               
                    item_parameters["typ"] = line[3 + i]
                    item_parameters["warehouse"] = line[4 + i]
                    item_parameters["exdate"] = line[5 + i]
                    item_parameters["supplytime"] = float(line[6 + i])
                    item_parameters["purchase price"] = float(line[7 + i])
                    item_parameters["purchase currency"] = line[8 + i]
                    item_parameters["purchase price unit"] = line[9 + i]
                    item_parameters["supplier"] = line[10 + i]
                    item_parameters["supplier name"] = line[11 + i]
                    item_parameters["nakupci"] = line[12 + i]
                    item_parameters["ordering system"] = line[13 + i]
                    item_parameters["safetystock"] = float(line[14 + i])
                    item_parameters["sales group"] = line[15 + i]            
                    item_parameters["sales lead time"] = int(line[16 + i])
                    item_parameters["sales price unit"] = line[17 + i]
                    item_parameters["routinglt"] = float(line[18 + i])
                    item_parameters["standardroutinglt"] = float(line[19 + i])
                    item_parameters["phantom"] = line[20 + i]
                    item_parameters["standard cost"] = float(line[21 + i])
                    item_parameters["material cost"] = float(line[22 + i])                
                    item_parameters["operation cost"] = float(line[23 + i])
                    item_parameters["bom qty"] = float(line[24 + i])

                    all_parameters[item] = item_parameters # Prida parametry prave reseneho itemu do parametru vsech itemu z reportu.
                    uz_projeto.append(item) # Prida prave reseny item do seznamu uz projetych itemu.
                                        
                    # B)
                    if all_parameters.get(item[9:len(item)]) == None: #Pokud neni jeste anonymni, rovnou vytvori anonymni polozku s daty z projektove polozky.
                        item_parameters["description"] = line[2 + i]               
                        item_parameters["typ"] = line[3 + i]
                        item_parameters["warehouse"] = line[4 + i]
                        item_parameters["exdate"] = line[5 + i]
                        item_parameters["supplytime"] = float(line[6 + i])
                        item_parameters["purchase price"] = float(line[7 + i])
                        item_parameters["purchase currency"] = line[8 + i]
                        item_parameters["purchase price unit"] = line[9 + i]
                        item_parameters["supplier"] = line[10 + i]
                        item_parameters["supplier name"] = line[11 + i]
                        item_parameters["nakupci"] = line[12 + i]
                        item_parameters["ordering system"] = line[13 + i]
                        item_parameters["safetystock"] = float(line[14 + i])
                        item_parameters["sales group"] = line[15 + i]            
                        item_parameters["sales lead time"] = int(line[16 + i])
                        item_parameters["sales price unit"] = line[17 + i]
                        item_parameters["routinglt"] = float(line[18 + i])
                        item_parameters["standardroutinglt"] = float(line[19 + i])
                        item_parameters["phantom"] = line[20 + i]
                        item_parameters["standard cost"] = float(line[21 + i])
                        item_parameters["material cost"] = float(line[22 + i])                
                        item_parameters["operation cost"] = float(line[23 + i])
                        item_parameters["bom qty"] = float(line[24 + i])
                    
                        all_parameters[item[9:len(item)]] = item_parameters # Prida parametry prave reseneho itemu do parametru vsech itemu z reportu.
                        uz_projeto.append(item[9:len(item)]) # Prida prave reseny item do seznamu uz projetych itemu.                        
                    
                    i += krok # Krok na dalsi item v lince. 1/2
                    item = line[1 + i] # Krok na dalsi item v lince. 2/2

            else: # Pokud se dil nebo jeho anonymni verze uz resil: 
                if item[0:3] != "PMP": # Pro anonymni dil.                  
                    if line[5 + i] == "19-JAN-38": # Prepise data, pokud ma reseny item platny expire date.
                        item_parameters["description"] = line[2 + i]               
                        item_parameters["typ"] = line[3 + i]
                        item_parameters["warehouse"] = line[4 + i]
                        item_parameters["exdate"] = line[5 + i]
                        item_parameters["supplytime"] = float(line[6 + i])
                        item_parameters["purchase price"] = float(line[7 + i])
                        item_parameters["purchase currency"] = line[8 + i]
                        item_parameters["purchase price unit"] = line[9 + i]
                        item_parameters["supplier"] = line[10 + i]
                        item_parameters["supplier name"] = line[11 + i]
                        item_parameters["nakupci"] = line[12 + i]
                        item_parameters["ordering system"] = line[13 + i]
                        item_parameters["safetystock"] = float(line[14 + i])
                        item_parameters["sales group"] = line[15 + i]            
                        item_parameters["sales lead time"] = int(line[16 + i])
                        item_parameters["sales price unit"] = line[17 + i]
                        item_parameters["routinglt"] = float(line[18 + i])
                        item_parameters["standardroutinglt"] = float(line[19 + i])
                        item_parameters["phantom"] = line[20 + i]
                        item_parameters["standard cost"] = float(line[21 + i])
                        item_parameters["material cost"] = float(line[22 + i])                
                        item_parameters["operation cost"] = float(line[23 + i])
                        item_parameters["bom qty"] = float(line[24 + i])
                    
                        all_parameters[item] = item_parameters # Prida parametry prave reseneho itemu do parametru vsech itemu z reportu.
                                               
                        i += krok # Krok na dalsi item v lince. 1/2
                        item = line[1 + i] # Krok na dalsi item v lince. 2/2
                    
                    elif line[5 + i] != "19-JAN-38": # Preskoci item, pokud ma reseny item NEplatny expire date. Rovnou se prejde na dalsi item.
                        i += krok # Krok na dalsi item v lince. 1/2
                        item = line[1 + i] # Krok na dalsi item v lince. 2/2

                elif item[0:3] == "PMP": # A) Pro projektovy dil rovnou doplni data. B) V anonymni polozce aktualizuje Routing LT a Standard routing LT.
                    # A)
                    item_parameters["description"] = line[2 + i]               
                    item_parameters["typ"] = line[3 + i]
                    item_parameters["warehouse"] = line[4 + i]
                    item_parameters["exdate"] = line[5 + i]
                    item_parameters["supplytime"] = float(line[6 + i])
                    item_parameters["purchase price"] = float(line[7 + i])
                    item_parameters["purchase currency"] = line[8 + i]
                    item_parameters["purchase price unit"] = line[9 + i]
                    item_parameters["supplier"] = line[10 + i]
                    item_parameters["supplier name"] = line[11 + i]
                    item_parameters["nakupci"] = line[12 + i]
                    item_parameters["ordering system"] = line[13 + i]
                    item_parameters["safetystock"] = float(line[14 + i])
                    item_parameters["sales group"] = line[15 + i]            
                    item_parameters["sales lead time"] = int(line[16 + i])
                    item_parameters["sales price unit"] = line[17 + i]
                    item_parameters["routinglt"] = float(line[18 + i])
                    item_parameters["standardroutinglt"] = float(line[19 + i])
                    item_parameters["phantom"] = line[20 + i]
                    item_parameters["standard cost"] = float(line[21 + i])
                    item_parameters["material cost"] = float(line[22 + i])                
                    item_parameters["operation cost"] = float(line[23 + i])
                    item_parameters["bom qty"] = float(line[24 + i])
                    
                    all_parameters[item] = item_parameters # Prida parametry prave reseneho itemu do parametru vsech itemu z reportu.                      
                    uz_projeto.append(item) # Prida prave reseny item do seznamu uz projetych itemu.

                    # B) Aktualizuje routing v anonymni polozce z reseneho projektoveho dilu. 
                    all_parameters[item[9:len(item)]]["routinglt"] = float(line[18 + i])
                    all_parameters[item[9:len(item)]]["standardroutinglt"] = float(line[18 + i]) 

                    i += krok # Krok na dalsi item v lince. 1/2
                    item = line[1 + i] # Krok na dalsi item v lince. 2/2
       
    return all_parameters            

# Vytvoreni kusovniku itemu jako list po jednotlivych linkach kusovniku. + Vytvoreni kusovniku s udajem ukazujicim realnou BOM qty.
def vytvoreni_kusovniku(data, krok, parameters):
    kusovnik_bom_qty = list()  # Kusovnik vsech linek:
    for line in data:
        line_valid = True # Overeni, zda linku pridavat do kusovniku, nebo ne.
        # print(line)
        i = 0
        kusovnik_linky_bom = []
        item = line[1]
        while item != "0":
            if line[5+i] == "19-JAN-38":
                kusovnik_linky_bom.append((item, float(line[24+i])))
                i += krok
                item = line[1+i]
            elif line[5+i] != "19-JAN-38":
                if len(kusovnik_linky_bom) == 0: # Pokud se jedna o vrchol s neplatnym Expiry date → nepridavat linku do kusovniku.
                    line_valid = False
                    break    
                elif item_typ(kusovnik_linky_bom[-1][0], parameters) == "P": # Pokud se jedna o neplatny poddil pod ciste nakupovanym dilem → pridat do kusovniku.
                    # kusovnik_linky_bom.append(item)
                    break
                elif je_to_man_placard(kusovnik_linky_bom[-1][0], parameters) or je_to_id_placard(kusovnik_linky_bom[-1][0], parameters): # Pokud se jedna o neplatny poddil pod pod MAN PLACARDEM → pridat do kusovniku.
                    kusovnik_linky_bom.append((item, float(line[24+i])))
                    break
                line_valid = False # Pokud se jedna o neplatny dil pod vyrabenym dilem a nesplnuje zadnou z podminek vyse → Nepridavat do kusovniku.
                break    

        if line_valid:
            if kusovnik_linky_bom not in kusovnik_bom_qty:
                kusovnik_bom_qty.append(kusovnik_linky_bom)  

    kusovnik_bez_bom_qty = [[item[0] for item in line] for line in kusovnik_bom_qty]
    
    return kusovnik_bez_bom_qty, kusovnik_bom_qty

def item_typ(item, parameters): 
    if (item[0:3] == "314") and (parameters.get(item).get("typ") == "Manufactured"):
        typ = "panel"
    elif (parameters.get(item).get("supplier") == "I00000008") and ((item[0] != "3") and (item[0] != "9" )): # Jedna se o nakupovany dil z Lamphunu a neni to surovy material.
        if parameters.get(item).get("warehouse") != "PZN110": # Neni to kanbanovka.
            typ = "M" 
        else:
            typ= "P" # Je to kanbanovka.             
    elif item[0:3] == "PMP": 
        if parameters.get(item).get("supplier") != "0" and parameters.get(item).get("nakupci") != "0": # PMP item, ktery ma purchase data a neni z lamphunu → nakuovany item
            typ = "P"
        else:    
            typ = "M"
    elif (parameters.get(item).get("nakupci") == "U5004258") and (parameters.get(item).get("supplier") == "0"): # Stanjur bez nastavenych purchase dat → na routingy.
        typ = "M"
    elif (parameters.get(item).get("nakupci") == "PZP001") and (parameters.get(item).get("supplier") == "0"): # Generic purchaser bez nastavenych purchase dat → na routingy.
        typ = "M"    
    elif parameters.get(item).get("supplier") != "0" and parameters.get(item).get("nakupci") != "0":          
        typ = "P"
    elif parameters.get(item).get("typ") == "Manufactured":        
        typ = "M"

    # elif (parameters.get(item).get("typ") == "Purchased") and (parameters.get(item).get("supplier") != "0") and (parameters.get(item).get("nakupci") != "0"):          
    #    typ = "P"

    # konkretni vyjimky itemy:
    elif item == "222516-15":
        typ = "P"
    else:
        typ = "N/A"
    return typ

def je_to_PMP_dil(item):
    return True if item[0:3] == "PMP" else False

def je_z_lamphunu(item, parameters):
    return True if parameters.get(item).get("supplier") == "I00000008" else False

def je_to_man_placard(item, parameters):
    nazev = parameters.get(item).get("description")
    man_placard = "placar"
    instalace   = "installation" 
    if (man_placard.upper() in nazev.upper()) and (parameters.get(item).get("typ") == "Manufactured"):
        if instalace.upper() not in nazev.upper():
            test = True
        else:
            test = False
    else:
        test = False
    return test

def je_to_id_placard(item, parameters):
    podminka = "ID PLACARD"
    if parameters.get(item).get("description") == podminka:
        return True
    return False

def level_pur_itemu(line, parameters, calc_mode):
    vyrabenych_dilu_v_lince = 0
    for item in line:
        if calc_mode == "nacenovani":
            typ = item_typ(item, parameters)
            if typ == "M":
                if len(line) > line.index(item) + 1:
                    if parameters.get(line[line.index(item)+1]).get("exdate") != "19-JAN-38" and not je_to_man_placard(item, parameters) and not je_to_id_placard(item, parameters):
                        print(f'Item {item} (safety stock {parameters.get(item).get("safetystock")}) v lince {line} ma pod sebou material {line[line.index(item)+1]} s neplatnym expiry date.')
                        print(f'Vyrabeny item {item}(ss {parameters.get(item).get("safetystock")}) pouze nakoupit.')
                        break
                    else:
                        vyrabenych_dilu_v_lince += 1       
                else:
                    vyrabenych_dilu_v_lince += 1
            else:
                break
        elif calc_mode == "ms":
            typ = item_typ(item, parameters)
            if typ == "M" or (typ =="P" and parameters.get(item) != None and (parameters.get(item).get("routinglt") != 0 or parameters.get(item).get("standardroutinglt") != 0)):
                if len(line) >= line.index(item):
                    if parameters.get(line[line.index(item)+1]).get("exdate") != "19-JAN-38":
                        print(f'item {item} (safety stock {parameters.get(item).get("safetystock")}) v lince {line} ma pod sebou material {line[line.index(item)+1]} s neplatnym expiry date.')
                        print(f'Vyrabeny item {item}(ss {parameters.get(item).get("safetystock")}) pouze nakoupit.')                       
                        break
                    else:
                        vyrabenych_dilu_v_lince += 1                      
                else:
                    vyrabenych_dilu_v_lince += 1
            else:
                break   
    if len(line) != vyrabenych_dilu_v_lince:
        prvni_nakupovany_poddil = line[vyrabenych_dilu_v_lince]
        level_prvniho_nakupovaneho_poddilu_linky = vyrabenych_dilu_v_lince + 1
    else:
        prvni_nakupovany_poddil = 0
        level_prvniho_nakupovaneho_poddilu_linky = 0
    #print("Prvni nakupovany poddil linky " + str(prvni_nakupovany_poddil))
    #rint("Level prvniho nakupovaneho poddilu linky " + str(level_prvniho_nakupovaneho_poddilu_linky)) 
    return [prvni_nakupovany_poddil, level_prvniho_nakupovaneho_poddilu_linky, vyrabenych_dilu_v_lince]

def routing_lt(line, parameters, missing_lts, calc_mode): # Urceni MAN LT podle kolik je tam projektovych dilu a dohledani jejich Routing LT.
    chyby_routing_lt = []
    vsechny_chybejici_routingy_linky = []
    vsechny_neplatne_routingy = []
    vsechny_spatne_item_typ = []
    vsechny_expired_date = []
    vsechny_use_polozky = []

    vyrabeny_lt_linky = 0
    manufactured_placard = False
    

    for item in line:
        typ = item_typ(item, parameters)
        #print(f'item typ {item} {typ}')
        
        if calc_mode == "nacenovani": # klasicke pocitani.
            if typ == "M": # Jedna se o MAN dil.
                if parameters.get(item).get("exdate") == "19-JAN-38": # S platnym expiry date.     
                    manufactured_placard = je_to_man_placard(item, parameters)
                    if manufactured_placard == True:
                        print(f'Vyrabeny item {item} v lince {line} je Manufactured PLACARD.')
                        vyrabeny_lt_linky += 2
                    elif (parameters.get(item).get("description")[0:4] == "USE ") or (" USE " in parameters.get(item).get("description")):
                        print(f'Vyrabeny item {item} v lince {line} je USE polozka. Tato linka se nepocita.')
                        vsechny_use_polozky.append(item)
                    elif parameters.get(item).get("phantom") == "Yes":
                        print(f'Vyrabeny item {item} v lince {line} je nastaven jako PHANTOM.')
                        if line.index(item) == 0:
                            vyrabeny_lt_linky += 3
                        else:
                            vyrabeny_lt_linky += 0
                    elif parameters.get(item).get("routinglt") != 0: # Dohledani routingu.
                        if parameters.get(item).get("routinglt") > 1999:
                            print(f'item {item} ma neplatny routing v LN. Tato linka se nepocita.')
                            vsechny_neplatne_routingy.append(item) 
                        else:
                            vyrabeny_lt_linky += parameters.get(item).get("routinglt")
                            vyrabeny_lt_linky += 3 # Pripocitava jeste 3 dni na kazdy vyrabeny dil na sestaveni.
                    elif parameters.get(item).get("standardroutinglt") != 0: # pripadne standard routingu.
                        if parameters.get(item).get("standardroutinglt") > 1999:
                            print(f'item {item} ma neplatny Standard routing v LN. Tato linka se nepocita.')
                            vsechny_neplatne_routingy.append(item)
                        else:
                            vyrabeny_lt_linky += parameters.get(item).get("standardroutinglt")
                            vyrabeny_lt_linky += 3
                    elif missing_lts !=0: # Pokud je nastaveno hromadne doplneni chybejicich routingu, bere hromadne nastavenu jako routing itemu.
                        if item not in vsechny_chybejici_routingy_linky:
                            vsechny_chybejici_routingy_linky.append(item)
                        vyrabeny_lt_linky += missing_lts
                        vyrabeny_lt_linky += 3                
                    else: # Rucni zadani routingu, pokud ho to nenaslo v CQ exportu.
                        if parameters.get(item).get("supplier") == "I00000008": # Informace, zda se jedna o Lamph. dil.
                            lamphun = "(Lamphun)"
                        else:
                            lamphun = "" 
                        if item[0:3] == "PMP":
                            pn = item[9:len(item)]
                            project = item[0:9]
                        else:
                            pn = item
                            project = ""                        
                        print("Pozor! vyrabeny item " + str(project)+" "+str(pn)+str(lamphun) + " v lince " + str(line) + " nema zadny Routing LT. Bud nema routing, nebo routing neni nacteny v CQ.")                    
                        if item not in vsechny_chybejici_routingy_linky:
                            vsechny_chybejici_routingy_linky.append(item)
                        while parameters.get(item).get("routinglt") == 0:
                            try:
                                chybejici_routing_lt = int(input("Je treba dopsat do zdrojoveho souboru k prvnimu vyskutu itemu " + str(item) + ", nebo zadej zde:\n"))
                                if chybejici_routing_lt > 0:
                                    parameters[item]["routinglt"] = chybejici_routing_lt  # Updatuje parametry itemu o chybejici udaj z inputu usera.
                                    vyrabeny_lt_linky += chybejici_routing_lt
                                    vyrabeny_lt_linky += 3
                                    print("LT updatovan: "+str(parameters.get(item).get("routinglt")))
                                    break
                                else: 
                                    print("LT musi byt kladne cele cislo (pocet dni).")                                        
                            except ValueError:
                                print("LT musi byt cislo (pocet dni).")  
                else:
                    print("Tato linka: " + str(line) + " se nepocita - vyrabeny dil " + str(item) + " nema platny Expiry date.\n")
                    vsechny_expired_date.append(item)
                    break
            elif typ == "N/A": # Neumime urcit typ itemu.
                # print(f'Nelze urcit typ itemu {item} v lince {line}. Tato linka se nepocita.')
                vsechny_spatne_item_typ.append(item)         
            else:
                break
        elif calc_mode == "ms": # MS pocitani.
            if typ == "M" or (typ =="P" and line.index(item) == 0 and parameters.get(item) != None and (parameters.get(item).get("routinglt") != 0 or parameters.get(item).get("standardroutinglt") != 0)): # Jedna se o MAN dil / P dil vyrobitelny u nas
                if typ == "M":
                    if parameters.get(item).get("exdate") == "19-JAN-38": # S platnym expiry date.     
                        manufactured_placard = je_to_man_placard(item, parameters)
                        if manufactured_placard == True:
                            print(f'Vyrabeny item {item} v lince {line} je Manufactured PLACARD.')
                            vyrabeny_lt_linky += 3
                        elif (parameters.get(item).get("description")[0:4] == "USE ") or (" USE " in parameters.get(item).get("description")):
                            print(f'Vyrabeny item {item} v lince {line} je USE polozka. Tato linka se nepocita.')
                            vsechny_use_polozky.append(item)
                        elif parameters.get(item).get("phantom") == "Yes":
                            print(f'Vyrabeny item {item} v lince {line} je nastaven jako PHANTOM.')
                            if line.index(item) == 0:
                                vyrabeny_lt_linky += 1 # Pro MS pocitani se phantomt pocitaji jeden den.
                            else:
                                vyrabeny_lt_linky += 1 # Pro MS pocitani se phantomt pocitaji jeden den.
                        elif parameters.get(item).get("routinglt") != 0: # Dohledani routingu.
                            if parameters.get(item).get("routinglt") > 1999:
                                print(f'item {item} ma neplatny routing v LN. Tato linka se nepocita.')
                                vsechny_neplatne_routingy.append(item) 
                            else:
                                vyrabeny_lt_linky += parameters.get(item).get("routinglt")
                        elif parameters.get(item).get("standardroutinglt") != 0: # pripadne standard routingu.
                            if parameters.get(item).get("standardroutinglt") > 1999:
                                print(f'item {item} ma neplatny Standard routing v LN. Tato linka se nepocita.')
                                vsechny_neplatne_routingy.append(item)
                            else:
                                vyrabeny_lt_linky += parameters.get(item).get("standardroutinglt")
                        elif missing_lts !=0: # Pokud je nastaveno hromadne doplneni chybejicich routingu, bere hromadne nastavenu jako routing itemu.
                            if item not in vsechny_chybejici_routingy_linky:
                                vsechny_chybejici_routingy_linky.append(item)
                            vyrabeny_lt_linky += missing_lts              
                        else: # Rucni zadani routingu, pokud ho to nenaslo v CQ exportu.
                            if parameters.get(item).get("supplier") == "I00000008": # Informace, zda se jedna o Lamph. dil.
                                lamphun = "(Lamphun)"
                            else:
                                lamphun = "" 
                            if item[0:3] == "PMP":
                                pn = item[9:len(item)]
                                project = item[0:9]
                            else:
                                pn = item
                                project = ""                        
                            print("Pozor! vyrabeny item " + str(project)+" "+str(pn)+str(lamphun) + " v lince " + str(line) + " nema zadny Routing LT. Bud nema routing, nebo routing neni nacteny v CQ.")                    
                            if item not in vsechny_chybejici_routingy_linky:
                                vsechny_chybejici_routingy_linky.append(item)
                            while parameters.get(item).get("routinglt") == 0:
                                try:
                                    chybejici_routing_lt = int(input("Je treba dopsat do zdrojoveho souboru k prvnimu vyskutu itemu " + str(item) + ", nebo zadej zde:\n"))
                                    if chybejici_routing_lt > 0:
                                        parameters[item]["routinglt"] = chybejici_routing_lt  # Updatuje parametry itemu o chybejici udaj z inputu usera.
                                        vyrabeny_lt_linky += chybejici_routing_lt
                                        print("LT updatovan: "+str(parameters.get(item).get("routinglt")))
                                        break
                                    else: 
                                        print("LT musi byt kladne cele cislo (pocet dni).")                                        
                                except ValueError:
                                    print("LT musi byt cislo (pocet dni).")  
                    else:
                        print("Tato linka: " + str(line) + " se nepocita - vyrabeny dil " + str(item) + " nema platny Expiry date.\n")
                        vsechny_expired_date.append(item)
                        break
                elif typ == "P": # Pokud se jedna o nakupovany vyrobitelny dil.
                    if parameters.get(item).get("exdate") == "19-JAN-38": # S platnym expiry date.    
                        if (parameters.get(item).get("description")[0:4] == "USE ") or (" USE " in parameters.get(item).get("description")):
                            print(f'Vyrabeny item {item} v lince {line} je USE polozka. Tato linka se nepocita.')
                            vsechny_use_polozky.append(item)
                        elif parameters.get(item).get("phantom") == "Yes":
                            print(f'Vyrabeny item {item} v lince {line} je nastaven jako PHANTOM.')
                            if line.index(item) == 0:
                                vyrabeny_lt_linky += 1
                            else:
                                vyrabeny_lt_linky += 1
                        elif parameters.get(item).get("routinglt") != 0: # Dohledani routingu.
                            if parameters.get(item).get("routinglt") > 1999:
                                print(f'item {item} ma neplatny routing v LN. Tato linka se nepocita.')
                                vsechny_neplatne_routingy.append(item) 
                            else:
                                vyrabeny_lt_linky += parameters.get(item).get("routinglt")
                        elif parameters.get(item).get("standardroutinglt") != 0: # pripadne standard routingu.
                            if parameters.get(item).get("standardroutinglt") > 1999:
                                print(f'item {item} ma neplatny Standard routing v LN. Tato linka se nepocita.')
                                vsechny_neplatne_routingy.append(item)
                            else:
                                vyrabeny_lt_linky += parameters.get(item).get("standardroutinglt")
                        else:
                            print(f'Vyrobitelna polozka {item} bez routingu v LN.')          
                    else:
                        print("Tato linka: " + str(line) + " se nepocita - vyrobitelny nakupovany dil " + str(item) + " nema platny Expiry date.\n")
                        vsechny_expired_date.append(item)
                        break         
            else:
                break

    # print("Vyrabent LT linky " + str(vyrabeny_lt_linky))   
    # print(seznam_itemu_s_chybejicim_routingem)   
    chyby_routing_lt.append(vsechny_chybejici_routingy_linky)
    chyby_routing_lt.append(vsechny_neplatne_routingy)
    chyby_routing_lt.append(vsechny_spatne_item_typ)
    chyby_routing_lt.append(vsechny_expired_date)
    chyby_routing_lt.append(vsechny_use_polozky)

    # print(f'chyby vyrabenych dilu linky {line} {chyby_routing_lt}')
    return [vyrabeny_lt_linky, chyby_routing_lt]

def purchased_lt(line, parameters, calc_mode): # Najde prvni nakupovany dil pod poslednim vyrabenym dilem, overi jeho platnost a ziska jeho PUR LT.
    # print(f'resena linka PLTL: {line}')
    chyby_purchased_lt = []
    nakupovane_dily_bez_purchase_dat = []
    nakupovane_dily_bez_lt = []
    nakupovane_expired_date = []
    nakupovane_use_polozky = []
    manufactured_dily_bez_kusovniku = []

    nakupovany_lt_linky = 0
    nejnizsi_nakupovany_dil_v_lince = level_pur_itemu(line, parameters, calc_mode)[0]
    # print(f' nejnizsi nak dil: {nejnizsi_nakupovany_dil_v_lince}')

    if calc_mode == "nacenovani":
        if nejnizsi_nakupovany_dil_v_lince == 0 and je_to_man_placard(line[len(line)-1], parameters) == False:
            print("Linka " + str(line) + " konci vyrabenym dilem s prazdnym kusovnikem. Tato linka se nepocita!\n")
            manufactured_dily_bez_kusovniku.append(line[len(line)-1])
        elif nejnizsi_nakupovany_dil_v_lince == 0 and je_to_man_placard(line[len(line)-1], parameters) == True:
            print("Linka " + str(line) + " konci MANUFACTURED PLACARDem.\n")
        else:
            if parameters.get(nejnizsi_nakupovany_dil_v_lince).get("exdate") == "19-JAN-38":            
                # konkretni vyjimky itemy:
                if nejnizsi_nakupovany_dil_v_lince == "222516-15":
                    print(f' Nakupovany poddil {nejnizsi_nakupovany_dil_v_lince} v lince {line} je spatne nastaven v LN (ma byt P15/350S). LT natvrdo prirazen 60 dni.')
                    nakupovany_lt_linky = 60            
                elif item_typ(nejnizsi_nakupovany_dil_v_lince, parameters) == "N/A":
                    nakupovany_lt_linky = 0
                elif item_typ(nejnizsi_nakupovany_dil_v_lince, parameters) == "panel":
                    nakupovany_lt_linky = 0
                elif (parameters.get(nejnizsi_nakupovany_dil_v_lince).get("description")[0:4] == "USE ") or (" USE " in parameters.get(nejnizsi_nakupovany_dil_v_lince).get("description")):
                    print(f'Tato linka: {line} se nepocita! Nakupovany dil {nejnizsi_nakupovany_dil_v_lince} je USE polozka.')
                    nakupovane_use_polozky.append(nejnizsi_nakupovany_dil_v_lince)    
                elif (parameters.get(nejnizsi_nakupovany_dil_v_lince).get("supplier") == "0") or (parameters.get(nejnizsi_nakupovany_dil_v_lince).get("nakupci") == "0"):
                    print(f'Tato linka: {line} se nepocita! Nakupovany dil {nejnizsi_nakupovany_dil_v_lince} nema v purchase datech vyplneny dodavatele nebo nakupciho. Je nutno poptat v nakupu.')
                    nakupovane_dily_bez_purchase_dat.append(nejnizsi_nakupovany_dil_v_lince)
                elif parameters.get(nejnizsi_nakupovany_dil_v_lince).get("phantom") == "Yes":
                    print("Nakupovany item " + str(nejnizsi_nakupovany_dil_v_lince) + " v lince " + str(line) + " je nastaven jako Phantom")
                    nakupovany_lt_linky = 0
                elif parameters.get(nejnizsi_nakupovany_dil_v_lince).get("warehouse") == "PZN110":
                    if line.index(nejnizsi_nakupovany_dil_v_lince) == 0:
                        nakupovany_lt_linky = parameters.get(nejnizsi_nakupovany_dil_v_lince).get("supplytime")
                    else:
                        nakupovany_lt_linky = 0
                elif nejnizsi_nakupovany_dil_v_lince in [
                    "3010086",
                    "3010088",
                    "3000011",
                    "3090024",
                    "3090557C",
                    "3120051"
                    ] and parameters.get(nejnizsi_nakupovany_dil_v_lince).get("safetystock") != 0:  # Overeni zda se jedna o surovy material se Safety stockem â†’ polud ano, LT 0.
                    nakupovany_lt_linky = 0
                elif parameters.get(nejnizsi_nakupovany_dil_v_lince).get("supplytime") != 0:
                    nakupovany_lt_linky = parameters.get(nejnizsi_nakupovany_dil_v_lince).get("supplytime")
                else:
                    nakupovane_dily_bez_lt.append(nejnizsi_nakupovany_dil_v_lince)
                    while True:
                        print("Pozor! Nakupovany dil " + str(nejnizsi_nakupovany_dil_v_lince) + " v lince " + str(line) + " ma v Purchase datech 0 LT!")
                        try:
                            chybejici_pur_lt = int(input("Dopln PUR LT pro " + str(nejnizsi_nakupovany_dil_v_lince) + " do txt. souboru, nebo zdej zde:\n"))
                            if chybejici_pur_lt > 0:
                                parameters[nejnizsi_nakupovany_dil_v_lince]["supplytime"] = chybejici_pur_lt  # Updatuje item o chybejici udaj z inputu usera.
                                nakupovany_lt_linky += chybejici_pur_lt
                                print("PUR LT updatovan.")
                                break
                            else:
                                print("PUR LT musi byt kladne cele cislo (pocet dni).")
                        except ValueError:
                            print("LT musi byt kladne cele cislo (pocet dni).")
                            continue
            elif parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("safetystock") != 0:
                print(f'item {line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]} (safety stock {parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("safetystock")}) v lince {line} ma pod sebou material {nejnizsi_nakupovany_dil_v_lince} s neplatnym expiry date.')
                print(f'Vyrabeny item {line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]}(ss {parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("safetystock")}) pouze nakoupit.')
                nakupovany_lt_linky = parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("supplytime")             
            elif je_to_man_placard(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1], parameters):
                print(f'MAM PLACARD {line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]} s nesmazanym kusovnikem')
                nakupovany_lt_linky = 0
            else:
                print("Tato linka: " + str(line) + " se nepocita - nakupovany dil " + str(nejnizsi_nakupovany_dil_v_lince) + " nema platny Expiry date.\n")
                nakupovane_expired_date.append(nejnizsi_nakupovany_dil_v_lince)
    if calc_mode == "ms":
        if nejnizsi_nakupovany_dil_v_lince == 0 and je_to_man_placard(line[len(line)-1], parameters) == False:
            print("Linka " + str(line) + " konci vyrabenym dilem s prazdnym kusovnikem. Tato linka se nepocita!\n")
            manufactured_dily_bez_kusovniku.append(line[len(line)-1])
        elif nejnizsi_nakupovany_dil_v_lince == 0 and je_to_man_placard(line[len(line)-1], parameters) == True:
            print("Linka " + str(line) + " konci MANUFACTURED PLACARDem.\n")
        else:
            if parameters.get(nejnizsi_nakupovany_dil_v_lince).get("exdate") == "19-JAN-38":            
                # konkretni vyjimky itemy:
                if nejnizsi_nakupovany_dil_v_lince == "222516-15":
                    print(f' Nakupovany poddil {nejnizsi_nakupovany_dil_v_lince} v lince {line} je spatne nastaven v LN (ma byt P15/350S). LT natvrdo prirazen 60 dni.')
                    nakupovany_lt_linky = 0            
                elif item_typ(nejnizsi_nakupovany_dil_v_lince, parameters) == "N/A":
                    nakupovany_lt_linky = 0
                elif item_typ(nejnizsi_nakupovany_dil_v_lince, parameters) == "panel":
                    nakupovany_lt_linky = 0
                elif (parameters.get(nejnizsi_nakupovany_dil_v_lince).get("description")[0:4] == "USE ") or (" USE " in parameters.get(nejnizsi_nakupovany_dil_v_lince).get("description")):
                    print(f'Tato linka: {line} se nepocita! Nakupovany dil {nejnizsi_nakupovany_dil_v_lince} je USE polozka.')
                    nakupovane_use_polozky.append(nejnizsi_nakupovany_dil_v_lince)    
                elif (parameters.get(nejnizsi_nakupovany_dil_v_lince).get("supplier") == "0") or (parameters.get(nejnizsi_nakupovany_dil_v_lince).get("nakupci") == "0"):
                    print(f'Tato linka: {line} se nepocita! Nakupovany dil {nejnizsi_nakupovany_dil_v_lince} nema v purchase datech vyplneny dodavatele nebo nakupciho. Je nutno poptat v nakupu.')
                    nakupovane_dily_bez_purchase_dat.append(nejnizsi_nakupovany_dil_v_lince)
                elif parameters.get(nejnizsi_nakupovany_dil_v_lince).get("phantom") == "Yes":
                    print("Nakupovany item " + str(nejnizsi_nakupovany_dil_v_lince) + " v lince " + str(line) + " je nastaven jako Phantom")
                    nakupovany_lt_linky += 1
                elif parameters.get(nejnizsi_nakupovany_dil_v_lince).get("warehouse") == "PZN110":
                    nakupovany_lt_linky = 0
                elif (nejnizsi_nakupovany_dil_v_lince[0] == "3" or nejnizsi_nakupovany_dil_v_lince[0] == "9") and parameters.get(nejnizsi_nakupovany_dil_v_lince).get("safetystock") != 0:  # Overeni zda se jedna o surovy material se Safety stockem â†’ polud ano, LT 0.
                    nakupovany_lt_linky = 0
                elif parameters.get(nejnizsi_nakupovany_dil_v_lince).get("supplytime") != 0:
                    nakupovany_lt_linky = 0
                else:
                    nakupovane_dily_bez_lt.append(nejnizsi_nakupovany_dil_v_lince)
                    print("Pozor! Nakupovany dil " + str(nejnizsi_nakupovany_dil_v_lince) + " v lince " + str(line) + " ma v Purchase datech 0 LT!")
            elif parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("safetystock") != 0:
                print(f'item {line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]} (safety stock {parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("safetystock")}) v lince {line} ma pod sebou material {nejnizsi_nakupovany_dil_v_lince} s neplatnym expiry date.')
                print(f'Vyrabeny item {line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]}(ss {parameters.get(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]).get("safetystock")}) pouze nakoupit.')
                nakupovany_lt_linky = 0            
            elif je_to_man_placard(line[line.index(nejnizsi_nakupovany_dil_v_lince)-1], parameters):
                print(f'MAM PLACARD {line[line.index(nejnizsi_nakupovany_dil_v_lince)-1]} s nesmazanym kusovnikem')
                nakupovany_lt_linky = 2
            else:
                print("Tato linka: " + str(line) + " se nepocita - nakupovany dil " + str(nejnizsi_nakupovany_dil_v_lince) + " nema platny Expiry date.\n")
                nakupovane_expired_date.append(nejnizsi_nakupovany_dil_v_lince)
    # print(f'PLT nakupovaneho itemu {nakupovany_lt_linky}')

    chyby_purchased_lt.append(nakupovane_dily_bez_purchase_dat)
    chyby_purchased_lt.append(nakupovane_dily_bez_lt)
    chyby_purchased_lt.append(nakupovane_expired_date)
    chyby_purchased_lt.append(nakupovane_use_polozky)
    chyby_purchased_lt.append(manufactured_dily_bez_kusovniku)    

    # print(f'chyby nakupovanuch dilu linky {line} {chyby_purchased_lt}')
    return [nakupovany_lt_linky, chyby_purchased_lt]

def lt_linky(line, parameters, missing_lts, calc_mode): # Vrati vysledny LT itemu a odpovidajici linku itemu.
    # print(f'Lt linky {line}')
    chyby_linky = []
      
    routing_lt_output = routing_lt(line, parameters, missing_lts, calc_mode)
    purchase_lt_output = purchased_lt(line, parameters, calc_mode)
    
    # print(f'routingLT output: {routing_lt_output}')
    # print(f'purchaseLT output: {purchase_lt_output}')
    error_chybejici_routingy_linky = routing_lt_output[1][0]
    error_neplatne_routingy_linky = routing_lt_output[1][1]
    error_type = routing_lt_output[1][2]
    error_expiry_date_rlt = routing_lt_output[1][3]
    error_use_polozky_rlt = routing_lt_output[1][4] 
    
    error_itemy_bez_purchase_dat = purchase_lt_output[1][0]
    error_itemy_bez_purchase_lt = purchase_lt_output[1][1]
    error_expiry_date_plt = purchase_lt_output[1][2]
    error_nakupovane_use_polozky = purchase_lt_output[1][3]
    error_manufactured_dily_bez_kusovniku = purchase_lt_output[1][4]
    lt_linky = routing_lt_output[0]+purchase_lt_output[0]

    chyby_linky.append(error_chybejici_routingy_linky)
    chyby_linky.append(error_neplatne_routingy_linky)
    if len(error_neplatne_routingy_linky) != 0:
        lt_linky = 0 
    chyby_linky.append(error_type)
    if len(error_type) != 0:
        lt_linky = 0 
    chyby_linky.append(error_expiry_date_rlt)
    if len(error_expiry_date_rlt) != 0:
        lt_linky = 0 
    chyby_linky.append(error_itemy_bez_purchase_dat)    
    if len(error_itemy_bez_purchase_dat) != 0:
        lt_linky = 0 
    chyby_linky.append(error_itemy_bez_purchase_lt)
    chyby_linky.append(error_expiry_date_plt)    
    if len(error_expiry_date_plt) != 0:
        lt_linky = 0
    chyby_linky.append(error_use_polozky_rlt)    
    if len(error_use_polozky_rlt) != 0:
        lt_linky = 0
    chyby_linky.append(error_nakupovane_use_polozky)    
    if len(error_nakupovane_use_polozky) != 0:
        lt_linky = 0
    chyby_linky.append(error_manufactured_dily_bez_kusovniku)    
    if len(error_manufactured_dily_bez_kusovniku) != 0:
        lt_linky = 0

    # print(f'vsechny chyby dilu linky {line} {chyby_linky}')
    # print(lt_linky)
    return [lt_linky, chyby_linky]
   
def nejdelsi_linka(line, parameters, calc_mode):
    lvl_pur_itemu = level_pur_itemu(line, parameters, calc_mode)[2]
    if lvl_pur_itemu != 0:
        nejdelsi_linka = line[0:(lvl_pur_itemu + 1)]
    else:
        nejdelsi_linka = line
    return nejdelsi_linka
      
def vysledek_itemu(nejdelsi_linka, parameters, vrchol, max_lt_itemu, missing_lts, vrchol_chyby, calc_mode): # sestaveni nejdelsi linky a jejiho LT. 
    # print(nejdelsi_linka)
    lt_nejdelsi_linky = []
    vysledek_itemu = ""
    # print(f'MLT i {max_lt_itemu}')
    if calc_mode == "nacenovani": # Vysledek kdyz se se pocita jako pro nacenovani.    
        if ((len(vrchol_chyby) == 1 and "error3" in vrchol_chyby) or len(vrchol_chyby) == 0) and max_lt_itemu != 0:
            if je_to_man_placard(vrchol, parameters) == True:
                # Pridani atributu production LT do parameters k itemu (placard)
                parameters[vrchol]["production lead time"] = 0
                # urceni sales LT na zaklade production LT (placard)
                sales_lt_itemu = 14
            else:
                # Pridani atributu production LT do parameters k itemu
                parameters[vrchol]["production lead time"] = max_lt_itemu
                # urceni sales LT na zaklade production LT
                sales_lt_itemu = int((max_lt_itemu/5+2)*7)
                if sales_lt_itemu <22:
                    sales_lt_itemu = 22 
            for item in nejdelsi_linka:
                typ = item_typ(item, parameters)
                if typ == "M": # and (parameters.get(item).get("warehouse") != "PZN110"):
                    if parameters.get(item).get("phantom") == "Yes":
                        lt_itemu = "MAN LT: " + "0 (phantom)" 
                    elif parameters[item].get("routinglt") != 0:
                        lt_itemu = "MAN LT: " + str(parameters[item].get("routinglt"))
                    elif parameters[item].get("standardroutinglt") != 0:
                        lt_itemu = "MAN LT: " + str(parameters[item].get("standardroutinglt"))
                    elif missing_lts != 0: 
                        lt_itemu = "MAN LT: " + str(missing_lts)+"(plosny routing)"
                    else: 
                        lt_itemu = "MAN LT: N/A"   
                    lt_nejdelsi_linky.append(lt_itemu)
                elif typ == "panel":
                    lt_itemu = f'PUR LT: {parameters[item].get("supplytime")} (panel)'
                    lt_nejdelsi_linky.append(lt_itemu)
                elif item in [
                    "3010086",
                    "3010088",
                    "3000011",
                    "3090024",
                    "3090557C",
                    "3120051"
                    ] and parameters.get(item).get("safetystock") != 0:
                    lt_itemu = "PUR LT: " + str(parameters[item].get("supplytime")) + " (safety stock: " + str(parameters[item].get("safetystock")) + ")"
                    lt_nejdelsi_linky.append(lt_itemu)
                else:
                    if parameters.get(item).get("warehouse") == "PZN110":
                        lt_itemu = f'PUR LT: {parameters[item].get("supplytime")} (PZN 110-kanban)'      
                    elif item[0:3] == "PMP" and typ == "P":                    
                        lt_itemu = f'PUR LT: {parameters[item].get("supplytime")} (ciste nakupovana)'
                    else:
                        lt_itemu = f'PUR LT: {parameters[item].get("supplytime")}'
                    lt_nejdelsi_linky.append(lt_itemu)
            if vrchol[0:3] == "PMP": # Jedna se o projektovy vrchol
                print("\nLinka s nejdelsim LT itemu "+ str(vrchol[0:9]) + " " + str(vrchol[9:len(vrchol)]) + ":\n" + str(nejdelsi_linka) +"\n" + str(lt_nejdelsi_linky))
            else: # Jedna se o anonymni vrchol
                print("\nLinka s nejdelsim LT itemu "+str(vrchol[0:len(vrchol)]) + ":\n" + str(nejdelsi_linka) +"\n" + str(lt_nejdelsi_linky))
            print("Production LT itemu " + str(nejdelsi_linka[0]) + ": " + str(max_lt_itemu) + " pracovnich dni.")
            print("Sales LT itemu " + str(nejdelsi_linka[0]) + ": " + str(sales_lt_itemu) + " kalendarnich dni.\n")
            if vrchol[0:3] == "PMP":
                vysledek_itemu = str(vrchol[0:9])+":"+str(vrchol[9:len(vrchol)])+" = "+str(int(sales_lt_itemu))
            else:
                if parameters.get(vrchol).get("supplier") == "I00000008":  
                    vysledek_itemu = "Lamphun_a:"+str(vrchol[0:len(vrchol)])+" = "+str(int(sales_lt_itemu))
                elif parameters.get(vrchol).get("supplier") != "0" and parameters.get(vrchol).get("nakukpci") != "0":
                    vysledek_itemu = "ciste_nak:"+str(vrchol[0:len(vrchol)])+" = "+str(int(sales_lt_itemu))             
                else :
                    vysledek_itemu = "anonymni_:"+str(vrchol[0:len(vrchol)])+" = "+str(int(sales_lt_itemu))     
        elif len(vrchol_chyby) != 0:
            sales_lt_itemu = "N/A"
            # Pridani atributu production LT do parameters k itemu (error)
            parameters[vrchol]["production lead time"] = "N/A"
            
            if vrchol[0:3] == "PMP":
                vysledek_itemu = f'{vrchol[0:9]}:{vrchol[9:len(vrchol)]} = '
            else:
                if parameters.get(vrchol).get("supplier") == "I00000008":  
                    vysledek_itemu = f'Lamphun_a:{vrchol[0:len(vrchol)]} = '
                else :
                    vysledek_itemu = f'anonymni_:{vrchol[0:len(vrchol)]} = '              
            if "error1" in vrchol_chyby:
                    # print('Neplatny routing na nekterem z dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Neplatny/e routing/gy.]  ' 
            if "error2" in vrchol_chyby:
                    # print('Neplatny typ itemu na nekterem z dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Neplatny typ itemu.]  ' 
            if "error3" in vrchol_chyby:
                    # print('Neplatny expiry date na nekterem z manufactured dilu vrcholu.')
                    vysledek_itemu += f'[Manufactured dil/y s neplatnym expire date.]  '         
            if "error4" in vrchol_chyby:
                    # print('Chybi purcahse data na nekterem z dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Chybi purchase data na nakupovanem dilu.]  '
            if "error5" in vrchol_chyby:
                    # print('Neplatny expiry date na nekterem z purchased dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Purchased dil/y s neplatnym expire date.]  '
            if "error6" in vrchol_chyby:
                    # print('Manufactured USE polozka vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Manufactured USE polozka vrcholu.]  '
            if "error7" in vrchol_chyby:
                    # print('nakupovana USE polozka vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Nakupovana USE polozka vrcholu.]  '
            if "error8" in vrchol_chyby:
                    # print('nakupovana USE polozka vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Manufactured dily bez kusovniku.]  '        
                        
        elif len(vrchol_chyby) == 0 and max_lt_itemu == 0:
            sales_lt_itemu = f'Nelze urcit'
            # Pridani atributu production LT do parameters k itemu (error)
            parameters[vrchol]["production lead time"] = "N/A"
            
            if vrchol[0:3] == "PMP":
                vysledek_itemu = f'{vrchol[0:9]}:{vrchol[9:len(vrchol)]} = {sales_lt_itemu}'
            else:
                if parameters.get(vrchol).get("supplier") == "I00000008":  
                    vysledek_itemu = f'Lamphun_a:{vrchol[0:len(vrchol)]} = {sales_lt_itemu}'
                elif parameters.get(vrchol).get("supplier") != "0" and parameters.get(vrchol).get("nakukpci") != "0":
                    vysledek_itemu = f'ciste_nak:{vrchol[0:len(vrchol)]} = {sales_lt_itemu}'             
                else :
                    vysledek_itemu = f'anonymni_:{vrchol[0:len(vrchol)]} = {sales_lt_itemu}'
            print(f'{vrchol} tady je to divny XXXX')            

    elif calc_mode == "ms": # Vysledek kdyz se se pocita jako na MS do vyroby.
        if ((len(vrchol_chyby) == 1 and "error3" in vrchol_chyby) or len(vrchol_chyby) == 0) and max_lt_itemu != 0:
            if je_to_man_placard(vrchol, parameters) == True:
                sales_lt_itemu = 3
            else:
                sales_lt_itemu = int(max_lt_itemu) + 3
            for item in nejdelsi_linka:
                typ = item_typ(item, parameters)
                if typ == "M": # and (parameters.get(item).get("warehouse") != "PZN110"):
                    if parameters.get(item).get("phantom") == "Yes":
                        lt_itemu = "MAN LT: " + "1 (phantom)" 
                    elif parameters[item].get("routinglt") != 0:
                        lt_itemu = "MAN LT: " + str(parameters[item].get("routinglt"))
                    elif parameters[item].get("standardroutinglt") != 0:
                        lt_itemu = "MAN LT: " + str(parameters[item].get("standardroutinglt"))
                    elif missing_lts != 0: 
                        lt_itemu = "MAN LT: " + str(missing_lts)+"(plosny routing)"
                    else: 
                        lt_itemu = "MAN LT: N/A"   
                    lt_nejdelsi_linky.append(lt_itemu)
                elif typ == "panel":
                    lt_itemu = f'PUR LT: {parameters[item].get("supplytime")} (panel)'
                    lt_nejdelsi_linky.append(lt_itemu)
                elif item in [
                    "3010086",
                    "3010088",
                    "3000011",
                    "3090024",
                    "3090557C",
                    "3120051"
                    ] and parameters.get(item).get("safetystock") != 0:
                    lt_itemu = "PUR LT: " + str(parameters[item].get("supplytime")) + " (safety stock: " + str(parameters[item].get("safetystock")) + ")"
                    lt_nejdelsi_linky.append(lt_itemu)
                elif typ == "P" and nejdelsi_linka.index(item) == 0 and (parameters.get(item).get("routinglt") != 0 or parameters.get(item).get("standardroutinglt") != 0):     
                    if parameters.get(item).get("routinglt") != 0:
                        lt_itemu = f'MAN LT: {parameters[item].get("routinglt")} (nakupovana vyrobitelna).'
                    elif parameters.get(item).get("standardroutinglt") != 0:
                        lt_itemu = f'MAN LT: {parameters[item].get("standardroutinglt")} (nakupovana vyrobitelna).'
                    lt_nejdelsi_linky.append(lt_itemu)                       
                else:
                    if parameters.get(item).get("warehouse") == "PZN110":
                        lt_itemu = f'PUR LT: {parameters[item].get("supplytime")} (PZN 110-kanban) (pocitam 0)'      
                    elif item[0:3] == "PMP" and typ == "P":                    
                        lt_itemu = f'PUR LT: {parameters[item].get("supplytime")} (ciste nakupovana) (pocitam 0)'
                    else:
                        lt_itemu = f'PUR LT: {parameters[item].get("supplytime") } (pocitam 0)'
                    lt_nejdelsi_linky.append(lt_itemu)
            if vrchol[0:3] == "PMP": # Jedna se o projektovy vrchol
                print("\nLinka s nejdelsim LT itemu "+ str(vrchol[0:9]) + " " + str(vrchol[9:len(vrchol)]) + ":\n" + str(nejdelsi_linka) +"\n" + str(lt_nejdelsi_linky))
            else: # Jedna se o anonymni vrchol
                print("\nLinka s nejdelsim LT itemu "+str(vrchol[0:len(vrchol)]) + ":\n" + str(nejdelsi_linka) +"\n" + str(lt_nejdelsi_linky))
            print("Production LT itemu " + str(nejdelsi_linka[0]) + ": " + str(max_lt_itemu) + " pracovnich dni.")
            print("Sales LT itemu " + str(nejdelsi_linka[0]) + ": " + str(sales_lt_itemu) + " kalendarnich dni.\n")
            if vrchol[0:3] == "PMP":
                vysledek_itemu = str(vrchol[0:9])+":"+str(vrchol[9:len(vrchol)])+" = "+str(int(sales_lt_itemu))
            else:
                if parameters.get(vrchol).get("supplier") == "I00000008":  
                    vysledek_itemu = "Lamphun_a:"+str(vrchol[0:len(vrchol)])+" = "+str(int(sales_lt_itemu))
                #elif parameters.get(vrchol).get("supplier") != "0" and parameters.get(vrchol).get("nakukpci") != "0":
                #    vysledek_itemu = "ciste_nak:"+str(vrchol[0:len(vrchol)])+" = "+str(int(sales_lt_itemu))             
                else :
                    vysledek_itemu = "anonymni_:"+str(vrchol[0:len(vrchol)])+" = "+str(int(sales_lt_itemu))     
        elif len(vrchol_chyby) != 0:
            sales_lt_itemu = "N/A"
            if vrchol[0:3] == "PMP":
                vysledek_itemu = f'{vrchol[0:9]}:{vrchol[9:len(vrchol)]} = '
            else:
                if parameters.get(vrchol).get("supplier") == "I00000008":  
                    vysledek_itemu = f'Lamphun_a:{vrchol[0:len(vrchol)]} = '
                else :
                    vysledek_itemu = f'anonymni_:{vrchol[0:len(vrchol)]} = '              
            if "error1" in vrchol_chyby:
                    # print('Neplatny routing na nekterem z dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Neplatny/e routing/gy.]  ' 
            if "error2" in vrchol_chyby:
                    # print('Neplatny typ itemu na nekterem z dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Neplatny typ itemu.]  ' 
            if "error3" in vrchol_chyby:
                    # print('Neplatny expiry date na nekterem z manufactured dilu vrcholu.')
                    vysledek_itemu += f'[Manufactured dil/y s neplatnym expire date.]  '         
            if "error4" in vrchol_chyby:
                    # print('Chybi purcahse data na nekterem z dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Chybi purchase data na nakupovanem dilu.]  '
            if "error5" in vrchol_chyby:
                    # print('Neplatny expiry date na nekterem z purchased dilu vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Purchased dil/y s neplatnym expire date.]  '
            if "error6" in vrchol_chyby:
                    # print('Manufactured USE polozka vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Manufactured USE polozka vrcholu.]  '
            if "error7" in vrchol_chyby:
                    # print('nakupovana USE polozka vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Nakupovana USE polozka vrcholu.]  '
            if "error8" in vrchol_chyby:
                    # print('nakupovana USE polozka vrcholu.') KRITICKA chyba
                    vysledek_itemu += f'[Manufactured dily bez kusovniku.]  '        
                        
        elif len(vrchol_chyby) == 0 and max_lt_itemu == 0:
            sales_lt_itemu = f'Nelze urcit'
            if vrchol[0:3] == "PMP":
                vysledek_itemu = f'{vrchol[0:9]}:{vrchol[9:len(vrchol)]} = {sales_lt_itemu}'
            else:
                if parameters.get(vrchol).get("supplier") == "I00000008":  
                    vysledek_itemu = f'Lamphun_a:{vrchol[0:len(vrchol)]} = {sales_lt_itemu}'
                #elif parameters.get(vrchol).get("supplier") != "0" and parameters.get(vrchol).get("nakukpci") != "0":
                #    vysledek_itemu = f'ciste_nak:{vrchol[0:len(vrchol)]} = {sales_lt_itemu}'             
                else :
                    vysledek_itemu = f'anonymni_:{vrchol[0:len(vrchol)]} = {sales_lt_itemu}'
            print(f'{vrchol} tadz xxxx')


    return vysledek_itemu

def chyby_linky(
    line,
    vrchol_chyby,
    lt_linky_output,
    vsechny_chybejici_routingy,
    vsechny_neplatne_routingy,
    vsechny_itemy_typ_error,
    vsechny_nakupovane_bez_puchase_dat,
    vsechny_nakupovane_bez_puchase_lt,
    vsechny_vyrabene_use_polozky,
    vsechny_nakupovane_use_polozky,
    vsechny_manufactured_dily_bez_kusovniku
):
            for item in lt_linky_output[1][0]:
                if item not in vsechny_chybejici_routingy:
                    vsechny_chybejici_routingy.append(item)
            for item in lt_linky_output[1][1]:
                if item not in vsechny_neplatne_routingy:
                   vsechny_neplatne_routingy.append(item)
            for item in lt_linky_output[1][2]:
                if item not in vsechny_itemy_typ_error:
                   vsechny_itemy_typ_error.append(item)
            for item in lt_linky_output[1][4]:
                if item not in vsechny_nakupovane_bez_puchase_dat:
                    vsechny_nakupovane_bez_puchase_dat.append(item)
            for item in lt_linky_output[1][5]:
                if item not in vsechny_nakupovane_bez_puchase_lt:    
                   vsechny_nakupovane_bez_puchase_lt.append(item)
            for item in lt_linky_output[1][7]:
                if item not in vsechny_vyrabene_use_polozky:    
                   vsechny_vyrabene_use_polozky.append(item)
            for item in lt_linky_output[1][8]:
                if item not in vsechny_nakupovane_use_polozky:
                    vsechny_nakupovane_use_polozky.append(item)
            for item in lt_linky_output[1][9]:
                if item not in vsechny_manufactured_dily_bez_kusovniku:
                    vsechny_manufactured_dily_bez_kusovniku.append(item)                                                            
            
            if len(lt_linky_output[1][1]) != 0:
                print(f'Pozor! itemy: {lt_linky_output[1][1]} v lince {line} maji neplatny routing. Tato linka se nepocita.')
                if 'error1' not in vrchol_chyby:
                    vrchol_chyby.append('error1')
            elif len(lt_linky_output[1][2]) != 0:
                print(f'Pozor! U itemu: {lt_linky_output[1][2]} v lince {line} nelze urcit typ (Manufactured / Purchased). Tato linka se nepocita.')
                if 'error2' not in vrchol_chyby:
                    vrchol_chyby.append('error2')
            elif len(lt_linky_output[1][3]) != 0:
                print(f'Pozor! Item: {lt_linky_output[1][3]} v lince {line} nema platny expiry date. Tato linka se nepocita.')
                if 'error3' not in vrchol_chyby:
                    vrchol_chyby.append('error3')
            elif len(lt_linky_output[1][4]) != 0:
                print(f'Pozor! nakupovane itemy: {lt_linky_output[1][4]} v lince {line} nemaji vyplneno suppliera nebo nakupciho. Tato linka se nepocita.')
                if 'error4' not in vrchol_chyby:
                    vrchol_chyby.append('error4')               
            elif len(lt_linky_output[1][6]) != 0:
                print(f'Pozor! nakupovane itemy: {lt_linky_output[1][6]} v lince {line} nemaji platny expiry date. Tato linka se nepocita.')
                if 'error5' not in vrchol_chyby:
                    vrchol_chyby.append('error5')
            elif len(lt_linky_output[1][7]) != 0:
                print(f'Pozor! vyrabene itemy: {lt_linky_output[1][7]} v lince {line} jsou USE polozky. Tato linka se nepocita.')
                if 'error6' not in vrchol_chyby:
                    vrchol_chyby.append('error6')
            elif len(lt_linky_output[1][8]) != 0:
                print(f'Pozor! nakupovane itemy: {lt_linky_output[1][8]} v lince {line} jsou USE polozky. Tato linka se nepocita.')
                if 'error7' not in vrchol_chyby:
                    vrchol_chyby.append('error7')
            elif len(lt_linky_output[1][9]) != 0:
                print(f'Pozor! vyrabene itemy: {lt_linky_output[1][9]} v lince {line} jsou Manufactured dily bez kusovniku a nejedna se o PLACARDY. Tato linka se nepocita.')
                if 'error8' not in vrchol_chyby:
                    vrchol_chyby.append('error8')                    

def linka_k_zaplanovani(line, parameters, polozky_pod_projekt_prepnout, platne_kalkulacni_projekty):
    #print(line)
    vse_v_lince = []
    for item in line:
        typ = item_typ(item, parameters)
        id_placard = je_to_id_placard(item, parameters)
        man_placard = je_to_man_placard(item, parameters)
        placard = f'(MAN PLACARD)' if id_placard or man_placard else ""
        #print(item)
        #print(typ)
        if typ == "M":
            #print(parameters.get(item).get("exdate"))
            if parameters.get(item).get("exdate") == "19-JAN-38":
                if parameters.get(item).get("phantom") == "Yes":
                    if item [0:3] == "PMP":
                        if placard:
                            item_to_plan = f'{item}(PHANTOM - PLACARD)'
                        else:
                            item_to_plan = f'{item}(PHANTOM)'
                        vse_v_lince.append(item_to_plan)
                    else:
                        if placard:
                            item_to_plan = f'PROJEKT_{item}(PHANTOM - PLACARD)'
                        else:
                            item_to_plan = f'PROJEKT_{item}(PHANTOM)'
                        vse_v_lince.append(item_to_plan)
                        if line[0][0:9] in platne_kalkulacni_projekty:
                            polozky_pod_projekt_prepnout.append(f'item {item}{placard}(PHANTOM) v lince {line}prepnout pod kalk. projekt')
                elif line.index(item)+1 != len(line): # Pokud linka nekonci vyrabenym itemem:
                    if parameters.get(line[line.index(item)+1]).get("exdate") != "19-JAN-38": # Pokud poddil nema platny expiry date:
                        if item_typ(line[line.index(item)+1], parameters) == "M": # Pokud se jedna o vyrabeny poddil s neplatnym EXdate → neplatna linka → ingnorovat.
                            return
                        elif parameters.get(item).get("safetystock") != 0:
                            if item [0:3] == "PMP":
                                item_to_plan = f'{item[9:len(item)]} manufactued dil s neplatnym materialem. Pouze nakoupit.(ss {parameters.get(item).get("safetystock")})'
                                vse_v_lince.append(item_to_plan)
                            else:
                                item_to_plan = f'{item} manufactued dil s neplatnym materialem. Pouze nakoupit.(ss {parameters.get(item).get("safetystock")})'
                                vse_v_lince.append(item_to_plan)
                    elif item [0:3] == "PMP":
                        item_to_plan = item
                        vse_v_lince.append(item_to_plan)
                    else:
                        item_to_plan = f'PROJEKT_{item}'
                        vse_v_lince.append(item_to_plan)
                        if line[0][0:9] in platne_kalkulacni_projekty:
                            polozky_pod_projekt_prepnout.append(f'item {item}{placard} v lince {line} prepnout pod kalk. projekt')
                elif item [0:3] == "PMP":
                    item_to_plan = item
                    vse_v_lince.append(item_to_plan)
                else:
                    item_to_plan = f'PROJEKT_{item}'
                    vse_v_lince.append(item_to_plan)
                    if line[0][0:9] in platne_kalkulacni_projekty:
                        polozky_pod_projekt_prepnout.append(f'item {item}{placard} v lince {line} prepnout pod kalk. projekt')
            else:
                return                
        elif typ == "P":
            if parameters.get(item).get("exdate") == "19-JAN-38":
                item_to_plan = item
                vse_v_lince.append(item_to_plan)
                break
            elif item_typ(line[line.index(item)-1], parameters) == "M":
                if parameters.get(line[line.index(item)-1]).get("safetystock") != 0:
                    item_to_plan = f'{item} Material s neplatnym expiry date. Vyrabeny naddil {line[line.index(item)-1]} pouze nakoupit(ss {parameters.get(item).get("safetystock")})'
                    vse_v_lince.append(item_to_plan)
                    break
                else:
                    item_to_plan = f'ERROR material {item} ma neplatny expiry date!'
                    vse_v_lince.append(item_to_plan)
                    break
            elif parameters.get(item).get("exdate") != "19-JAN-38":
                item_to_plan = f'ERROR material {item} ma neplatny expiry date!'
                vse_v_lince.append(item_to_plan)
                break
        elif typ == "panel":
            item_to_plan = item
            vse_v_lince.append(item_to_plan)            
        elif typ == "N/A":
            item_to_plan = f'ErrorType {item}'
            vse_v_lince.append(item_to_plan)
    # if (len(vse_v_lince) == 1) and (vse_v_lince[0][0:3] == "PMP" or vse_v_lince[0][0:9] == "PROJEKT_") and ("PLACARD" not in vse_v_lince[0]) and ("PHANTOM" not in vse_v_lince[0]):
    if len(vse_v_lince) == 1:
        if (vse_v_lince[0][0:3] == "PMP" or vse_v_lince[0][0:8] == "PROJEKT_") and ("PLACARD" not in vse_v_lince[0]):
            pass      
        else:
            return(vse_v_lince)
    else:
        return(vse_v_lince)

#def zaplanovani_do_excelu(vse_k_zaplanovani):
#    # print(vse_k_zaplanovani)
#    wb = excel.load_workbook('C:\\Users\\Ondrej.rott\\Documents\\Python\\Pracovni\\to_plan.xlsx')
#    sheet1 = wb["K zaplanovani do LN"]
#    radek_itemu_to_plan = 2
#    sloupec_itemu_to_plan = 1
#   
#    for row in sheet1:
#        sheet1.delete_rows(2,sheet1.max_row)
#    for linka in vse_k_zaplanovani:
#        if vse_k_zaplanovani.index(linka) == 0: # prvni linka k zaplanovani
#            current_vrchol = linka[0]
#            for item in linka:       
#                cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                cell_to_plan.value = item
#                sloupec_itemu_to_plan += 1
#            radek_itemu_to_plan += 1
#            sloupec_itemu_to_plan = 1        
#        else: # nejedna se o prvni linku k zaplanovani
#            for item in linka:
#                try:
#                    if  linka.index(item) == 0: # pro prvni item v lince je test jiny nez pro zbytek 
#                        if item == current_vrchol:
#                            cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                            cell_to_plan.value = item
#                            sloupec_itemu_to_plan += 1
#                        else:
#                            current_vrchol = item
#                            cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                            cell_to_plan.value = item
#                            sloupec_itemu_to_plan += 1
#                    # elif not(len(linka) > len(vse_k_zaplanovani[vse_k_zaplanovani.index(linka)-1])): # predchozi linka nesmi byt kratsi nez tato. (muze se jednat o pokracovani predchoziho poddilu)
#                    elif item == vse_k_zaplanovani[vse_k_zaplanovani.index(linka)-1][linka.index(item)+linka[0:sloupec_itemu_to_plan-1].count(item)]: #pokud je item stejny jako ten nad nim
#                        if sheet1.cell(radek_itemu_to_plan, sloupec_itemu_to_plan -1).value == None: # pokud bunka v excelu vlevo od itemu je prazdna (jedna se o poddil predchoyiho itemu) 
#                            cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                            cell_to_plan.value = None # None → pokracovni dilu nad timto
#                            sloupec_itemu_to_plan += 1
#                        else: 
#                            cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                            cell_to_plan.value = item # jedna se o stejny dil jako nad nim, ale pod jinym vrcholem → zaplanovat
#                            sloupec_itemu_to_plan += 1
#                    else:
#                        cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                        cell_to_plan.value = item # jedna se o stejny dil jako nad nim, ale pod jinym vrcholem → zaplanovat
#                        sloupec_itemu_to_plan += 1
#                except:
#                    cell_to_plan = sheet1.cell(radek_itemu_to_plan,sloupec_itemu_to_plan)
#                    cell_to_plan.value = item # jedna se o stejny dil jako nad nim, ale pod jinym vrcholem → zaplanovat
#                    sloupec_itemu_to_plan += 1
#            radek_itemu_to_plan +=1
#            sloupec_itemu_to_plan = 1
#    wb.save("C:\\Users\\Ondrej.rott\\Documents\\Python\\Pracovni\\to_plan.xlsx")

def lokalni_dodavatele(item, parameters):
    lok_dodavatele_name = (
    "Carry Goods s.r.o.",
    "Elakov Production s.r.o.",
    "EVEKTOR-AEROTECHNIK a.s.",
    "HT Metal s.r.o.",
    "LABARA s.r.o.",
    "PRIMAPOL-METAL-SPOT, s.r.o.",
    "STARTECH s.r.o.",
    "Tuma aerospace s.r.o.",
    "Workpress Aviation s.r.o.",
    "Safran Cabin Lamphun Ltd.",
    "Molins a.s.",
    "SW-MOTECH s.r.o.",
    "STARTECH s.r.o.",
    "AXA CNC stroje, s.r.o."
    )

    if parameters.get(item).get("supplier name") in lok_dodavatele_name:
        return True
    else:
        return False

def catalogue_design_dodavatele_BFE(item, parameters):
    # Seznam v BFE nacenovani "List of suppliers"
    catalogue_dodavatele = (
        "E20001409",
        "E20000463",
        "E20000407",
        "E20000225",
        "E20000371",
        "E20002038",
        "E20000245",
        "E20000273",
        "E20000192",
        "E20000222",
        "E20001929",
        "E20000577",
        "E20000427",
        "E20001016",
        "E20000308",
        "E20000322",
        "E20000361",
        "E20001231",
        "E20000187",
        "E20000419",
        "E20001252",
        "E20000227",
        "E20000501",
        "E20000188",
        "E20000483",
        "E20000202",
        "E20000217",
        "E20000422",
        "E20000416",
        "E21000454",
        "E20000305",
        "E20000348",
        "E20000246",
        "E20000382",
        "E20000398",
        "E20000360",
        "E21000457",
        "E21000455",
        "E20000401",
        "E20000345",
        "E20000255",
        "E20000670"         
    )

    if parameters.get(item).get("supplier") in catalogue_dodavatele:
        return True
    else:
        return False        

def nakupovany_costing_ok(vrchol, parameters, kusovnik): # Zkontroluje, jestli nejaky nakupovany dil pod nacenovanym vrcholem ma chybejici standard cost.
                                                    # Vrati True / False, pripadne seznam dilu s 0 standard cost.
    nakupovane_poddily_missing_scp = [f'{item}' for line in [line for line in kusovnik if line[0] == vrchol] for item in line if item[0:3] != "PMP" and parameters.get(item).get("standard cost") == 0]
    nakupovane_poddily_missing_scp = list(dict.fromkeys(nakupovane_poddily_missing_scp)) # Vytvori z listu Dictionary a pak zpatky list (odstraneni duplicit)
    check = True if len(nakupovane_poddily_missing_scp) == 0 else False
    return check, nakupovane_poddily_missing_scp

def pmp_costing_ok(vrchol, parameters, kusovnik): # Zkontroluje, jestli nejaky PMP dil pod nacenovanym vrcholem ma chybejici routing → spatny routing / nezkalkulovany dil.
                                                    # Vrati True / False, pripadne seznam dilu bez routingu
    pmp_poddily_missing_routing = [f'{item[0:9]} {item[9:len(item)]}' for line in [line for line in kusovnik if line[0] == vrchol] for item in line if item[0:3] == "PMP" and parameters.get(item).get("routinglt") == 0 and parameters.get(item).get("standardroutinglt") == 0]
    pmp_poddily_missing_routing = list(dict.fromkeys(pmp_poddily_missing_routing)) # Vytvori z listu Dictionary a pak zpatky list (odstraneni duplicit)
    check = True if len(pmp_poddily_missing_routing) == 0 else False
    return check, pmp_poddily_missing_routing

def bom_qty_ok(vrchol, parameters, kusovnik_bom_qty): # Zkontorluje, zda nejaky dil pod nacenovanym vrcholem nema 0 mnozstvi materialu v kusovniku. Pokud ano, vrati vrchol jako chybu kusovniku.
    error_bom_qty = set()    
    for line in kusovnik_bom_qty:
        if line[0][0] == vrchol:
            for item in line:
                if je_to_man_placard(item[0], parameters) or je_to_id_placard(item[0], parameters): # Pro MAN placard overi, ze pod sebou nema zadny poddil. Pokud ano → chyba smazat kusovnik PLACARDU.
                    if len(line) > line.index(item)+1:
                        print(f' POZOR! Vyrabeny PLACARD {item[0]} v lince {line} ma pod sebou nesmazany kusovnik.')
                        error_bom_qty.add((item[0], str(line)))
                
                 # Pro vyrabene dily overi, ze jejich poddil nema 0 qty BOM. Pokud ano → chyba 0 qty kusovniku itemu.
                if item[0][0:3] == "PMP": # PMP vyrabene veci.
                    if item_typ(item[0][9:len(item[0])], parameters) == "M":
                        if len(line) > line.index(item)+1:
                            if line[line.index(item)+1][1] == 0:
                                print(f' POZOR! Vyrabeny item {item[0]} v lince {line} ma pod sebou poddil/material s 0 qty BOM.')
                                error_bom_qty.add((item[0], str(line)))
                if item[0][0:3] != "PMP": # anonymni vyrabene veci.
                    if item_typ(item[0], parameters) == "M":
                        if len(line) > line.index(item)+1:
                            if line[line.index(item)+1][1] == 0:
                                print(f' POZOR! Vyrabeny item {item[0]} v lince {line} ma pod sebou poddil/material s 0 qty BOM.')
                                error_bom_qty.add((item[0], str(line)))               
                    # if parameters.get(item[0]).get("phantom").upper() == "YES":
    check = True if len(error_bom_qty) == 0 else False
    return check, error_bom_qty
           
def naceneni_do_tabulek(vrchol, parameters, program, kusovnik, kusovnik_bom_qty):
    # print(f'program {vrchol} {program}')
    typ = item_typ(vrchol, parameters)
    
    lok_dod = lokalni_dodavatele(vrchol, parameters)
    # print(f'{vrchol} lok dod {lok_dod}')
    
    catalogue_design_BFE = catalogue_design_dodavatele_BFE(vrchol, parameters)
    # print(f'{vrchol} cat dod {catalogue_design_BFE}')
    
    is_man_placard = je_to_man_placard(vrchol, parameters)
    
    is_ID_placard = je_to_id_placard(vrchol,parameters)
    
    # kontrola jestli vsechny nakupovane poddily vrholu maji nenulovu standard cost.
    purchased_standard_costing_check = nakupovany_costing_ok(vrchol, parameters, kusovnik)
    # print(f'pur SCP 0 check: {purchased_standard_costing_check}')

    # kontrola jestli vsechny vyrabene poddily vrholu maji nenulovu operation cost.
    pmp_operation_costing_check = pmp_costing_ok(vrchol, parameters, kusovnik)
    # print(f'routing 0 check: {pmp_operation_costing_check}')
    
    # kontrola jestli vsechny poddily maji nenulove mnozstvi nastavene v kusovniku.
    bom_qty_check = bom_qty_ok(vrchol, parameters, kusovnik_bom_qty)
    # print(f'TADY {bom_qty_check}')

    # PxM pole    
    # Nakupovane dily    
    if typ == "P":            
        # Od lokalnich dodavatelu nacenit jako vyrabene.
        if lok_dod == True:
            if program == "SFE" or program == "MIX":
                pxm_pole = "M"
            elif program == "BFE":
                pxm_pole = "Make"
            else:
                pxm_pole = "N/A (Vyrabena)"
        if lok_dod == False:
            if program == "SFE" or program == "MIX":
                pxm_pole = "P"
            elif program == "BFE":
                pxm_pole = "Buy"
            else:
                pxm_pole = "N/A (Kupovana)"                
    # Vyrabene dily
    elif typ == "M":
        # Lamphun
        if lok_dod == True:
            # Lamphunova SIC polozka → P
            if parameters.get(vrchol).get("ordering system") == "SIC":
                if program == "SFE" or program == "MIX":
                    pxm_pole = "P"
                elif program == "BFE":
                    pxm_pole = "Buy"
                else:
                    pxm_pole = "N/A (Kupovana)"                         
            else:
                if program == "SFE" or program == "MIX":
                    pxm_pole = "M"
                elif program == "BFE":
                    pxm_pole = "Make"
                else:
                    pxm_pole = "N/A (Vyrabena)" 
        else:
            if program == "SFE" or program == "MIX":
                pxm_pole = "M"
            elif program == "BFE":
                pxm_pole = "Make"
            else:
                pxm_pole = "N/A (Vyrabena)" 
    # lokalni dodavatel pole
    if lok_dod == True:
        if vrchol[0:3] == "PMP":
            lok_dod_pole = parameters.get(vrchol[9:len(vrchol)]).get("supplier name")
        else:
            lok_dod_pole = parameters.get(vrchol).get("supplier name")
    else:
        lok_dod_pole = ""
    # ID placard pole
    if is_ID_placard == True:
        id_placard_pole = "YES"
    else:
        id_placard_pole = "NO"
    # Brady placard pole
    if is_man_placard == True and is_ID_placard == False:
        brady_placard_pole = "YES"
    else:
        brady_placard_pole = "NO"  
    # pocet placardovych instalaci pole
        # nereseno

    # supplier name pro "our design" (BFE only)
    if program == "BFE":
        if catalogue_design_BFE == True:
            if vrchol[0:3] == "PMP":
                catalogue_dod_pole = parameters.get(vrchol[9:len(vrchol)]).get("supplier name")
            else:
                catalogue_dod_pole = parameters.get(vrchol).get("supplier name")
        else:
            catalogue_dod_pole = ""
    else:
            catalogue_dod_pole = ""        
    # PN pole
    if vrchol[0:3] == "PMP":
        pn_pole = vrchol[9:len(vrchol)]
    else:
        pn_pole = vrchol
    # description pole         
    description_pole = parameters.get(vrchol).get("description")
    # unit pole 
    if vrchol[0:3] == "PMP":
        unit_pole = parameters.get(vrchol[9:len(vrchol)]).get("sales price unit")
    else:
        unit_pole = parameters.get(vrchol).get("sales price unit")
    # production LT pole
    production_lt_pole = parameters.get(vrchol).get("production lead time")
    # date of entry pole
    entry_date_pole = date.today().strftime("%d/%m/%Y").replace("/", ".")
    # EUR cost price
    if is_man_placard or is_ID_placard:
        cost_eur_pole = f'MAN PLACARD'
    # kontrola costingu vyrabenych polozek.
    elif vrchol[0:3] == "PMP":
        cost_eur_pole_errors = list()
        # check 0 costy materialu vrcholu
        if parameters.get(vrchol).get("material cost") == 0:
            cost_eur_pole_errors.append("VRCHOL missing material cost")
        # check chybejicich routingu
        if not pmp_operation_costing_check[0]:
            cost_eur_pole_errors.append(f'missing routing on MAN items {pmp_operation_costing_check[1]}')
        # check chybejicich costu nakupovanych polozek
        if not purchased_standard_costing_check[0]:
            cost_eur_pole_errors.append(f'missing standard cost on PUR items {purchased_standard_costing_check[1]}')
        # Pokud nenaslo zadne chyby → vzit costing z vrcholu jako platnz EUR costing.
        if len(cost_eur_pole_errors) == 0:
            cost_eur_pole = parameters.get(vrchol).get("standard cost")
        # Jinak vratit misto costu seznam chyb
        else:
            cost_eur_pole = cost_eur_pole_errors    
    else:
        if parameters.get(vrchol).get("material cost") == 0:
            cost_eur_pole = "missing material cost"
        else:
            purchase_price = parameters.get(vrchol).get("purchase price")
            purchase_currency = parameters.get(vrchol).get("purchase currency")
            purchase_units = parameters.get(vrchol).get("purchase price unit")

            rates_to_eur_2022 = {
                "USD": 1.16,
                "EUR": 1,
                "CZK": 24.36,
                "GBP": 0.89
            }
            non_standard_units = {
                "MIL": 1000,
                "HEC": 100
            }

            # Pokud je nestandardni jednotka, nejprve vydelit na 1 ea.
            if purchase_units.upper() in non_standard_units:
                purchase_price = purchase_price / non_standard_units.get(purchase_units.upper())
            # Pote pokud curency neni euro, prepocist na eura.
            purchase_price_eur_1unit = purchase_price / rates_to_eur_2022.get(purchase_currency.upper())

            cost_eur_pole = round(purchase_price_eur_1unit,2) 
    return [pxm_pole, lok_dod_pole, id_placard_pole, brady_placard_pole, "", catalogue_dod_pole, pn_pole, description_pole, unit_pole, production_lt_pole, entry_date_pole, cost_eur_pole], bom_qty_check