#!/usr/bin/env python

# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 3
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


from tinydb import TinyDB, Query, where
from parser import getFilePaths


def main():
    # Dictionaries done thanks to the parsing of the txt microscope script:

    """
    ars = [{'filename': "1.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 740,
         'angle': 30, 'repetition': 1, 'FF': False},
        {'filename': "2.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 40, 'repetition': 2, 'FF': False},
        {'filename': "3.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 50, 'repetition': 3, 'FF': False},
        {'filename': "4.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 740,
         'angle': 60, 'repetition': 4, 'FF': False},
        {'filename': "5.xrm", 'sample': 'tomo1', 'zp': 7, 'energy': 520,
         'angle': 450, 'repetition': 5, 'FF': False},
        {'filename': "6.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 300, 'repetition': 1, 'FF': False},
        {'filename': "7.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 4000, 'repetition': 2, 'FF': False},
        {'filename': "8.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 50000, 'repetition': 3, 'FF': False},
        {'filename': "9.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 6000000000, 'repetition': 4, 'FF': False},
        {'filename': "10.xrm", 'sample': 'tomo1', 'zp': 7, 'energy': 520,
         'angle': 5000, 'repetition': 5, 'FF': False},
        {'filename': "11.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 3000000, 'repetition': 1, 'FF': False},
        {'filename': "12.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 400, 'repetition': 2, 'FF': False},
        {'filename': "13.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 50000, 'repetition': 3, 'FF': False},
        {'filename': "14.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 6000, 'repetition': 4, 'FF': False},
        {'filename': "15.xrm", 'sample': 'tomo1', 'zp': 7, 'energy': 520,
         'angle': 500, 'repetition': 5, 'FF': False},
        {'filename': "16.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 740,
         'angle': 3, 'repetition': 1, 'FF': False},
        {'filename': "17.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 4, 'repetition': 2, 'FF': False},
        {'filename': "18.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 5, 'repetition': 3, 'FF': True},
        {'filename': "19.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 740,
         'angle': 6, 'repetition': 4, 'FF': True},
        {'filename': "20.xrm", 'sample': 'tomo1', 'zp': 7, 'energy': 520,
         'angle': 5, 'repetition': 5, 'FF': True}]
    """

    #parser = ParserTXMScript()
    #collected_images = parser.parse_script("many_folder.txt")



    Files = Query()
    query_impl = ((Files.energy > 400) & (Files.energy <= 500) & (Files.angle > -15) & (Files.angle <= 100))
    files = getFilePaths("many_folder.txt", query_impl, only_existing=True) #, root_path="/home/mrosanes/PycharmProjects/txmparser/rootfolder")
    for i in files:
        print(i)
        print("\n")







    

    
    """
    #& (Files.angle > -10) & (Files.angle <= 0))

    #prettyprinter = pprint.PrettyPrinter(indent=4)
    #prettyprinter.pprint(collected_images)
    
    #print(found_files)

    #print(found_files)
    
    #found_files = db.search((Files.energy == 500))
    #found_files = db.search((Files.energy == 425) & (Files.FF == True) &
    #                        (Files.angle > -10) & (Files.angle <= 0))
    #found_files = db.search((Files.repetition == 2) & (Files.FF == False) &
    #                        (Files.date == 20171113))
    #found_files = db.search((Files.FF == True) &
    #                        (Files.energy > 350) & (Files.energy <= 450)) 
    
    from operator import itemgetter
    # Used to organize numbers in increasing or decreasing order
    result = sorted(found_files, key=itemgetter('energy'), reverse=False)
    
    #print(result)
        
    for entry in result:
        pass
        #print(entry["filename"])
        #print(entry["subfolder"])
        
    root_folder = "/home/mrosanes/PycharmProjects/txmparser/rootfolder"
    query = result
    #print(query)
    
    file_paths = indexer.getFilePaths(root_folder, query, True) #False) #True#)   
    for file_path in file_paths:
        print("\n")
        print(file_path)
    
    found2 = db.search(Files.zpz < 1)
    #print(found2)
    
    
    found3 = db.search(Files.zp.exists())
    #print(found3)
    
    res2 = sorted(found2, key=itemgetter('zpz'), reverse=False)
    zpz_all_files = [] 
    for entry in res2:
        pass
        #try:
            
        #print(entry["zpz"])
    
    
    for entry in result:
        pass
        #print(entry["filename"])
    db.close()
    
    #with open('db.json') as data_file:
    #    data = json.load(data_file)
    #print(data)
    """

if __name__ == "__main__":
    main()

