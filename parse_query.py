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

import os
import pprint
from operator import itemgetter
from tinydb import TinyDB, Query, where
from parser import get_db, get_file_paths, search_and_get_file_paths


def main():
    # Dictionaries done thanks to the parsing of the txt microscope script:

    """
    query_output_example = 
       [{'filename': "1.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 740,
         'angle': 30, 'repetition': 1, 'FF': False},
        {'filename': "2.xrm", 'sample': 'tomo1', 'zp': 3, 'energy': 520,
         'angle': 40, 'repetition': 2, 'FF': False},
        {'filename': "3.xrm", 'sample': 'tomo1', 'zp': 5, 'energy': 520,
         'angle': 50, 'repetition': 3, 'FF': False}]
    """

    prettyprinter = pprint.PrettyPrinter(indent=4)


    #query_impl = ((Files.energy > -100) & (Files.energy <= 800) &
    #(Files.angle > -360) & (Files.angle <= 360))

    
    #txm_txt_script = "many_folder.txt"
    #txm_txt_script = "txm_script_1.txt"
    txm_txt_script = "txm_script_2.txt"
    root_path = os.path.dirname(os.path.abspath(txm_txt_script))
    
    db = get_db(txm_txt_script, use_existing_db=False)
    #query_output = db.search(query_impl)
    
    #for i in query_output:
    #    print(i)
    #    print("\n") 
    
    
     
    
    all_file_records = db.all()
    #print(all_file_records[0])
    Files = Query()

    energies_from_all_files = [record["energy"] for record in all_file_records]
    energies_exisiting = sorted(set(energies_from_all_files))
    print(energies_exisiting)
    print("\n")
    
    dates_samples_energies = []
    for record in all_file_records:
        dates_samples_energies.append(record["sample"] + "_" + 
                                      str(record["date"]) + "_" + 
                                      str(record["energy"]))                         
    dates_samples_energies = list(set(dates_samples_energies))
    
    print(dates_samples_energies)
    print("\n")
    
    

    many_tomos_experiment_files = {}

    for date_sample_energie in dates_samples_energies:
        print(date_sample_energie)
        files_by_zp = {}
        files_for_sample_subdict = {}

        energy = date_sample_energie.split('_')[-1]
        energy = float(energy)
        query_impl = (Files.energy == energy)
        records_by_given_energy = db.search(query_impl)

        zps_for_given_energy = [record["zpz"] for record in 
                                records_by_given_energy]
        zpz_positions_for_given_energy = sorted(set(zps_for_given_energy))     
        
        for zpz in zpz_positions_for_given_energy:
            query_impl = ((Files.energy == energy) & (Files.zpz == zpz) & 
                          (Files.FF == False))
            fn_by_zpz_query = db.search(query_impl)
            sorted_fn_by_zpz_query = sorted(fn_by_zpz_query, 
                                            key=itemgetter('angle'))
            
            files = get_file_paths(sorted_fn_by_zpz_query, root_path, 
                                   use_subfolders=True,
                                   only_existing_files=False)       
            files_by_zp[zpz] = files
            
        # Get FF image records
        fn_ff_query_by_energy = ((Files.energy == energy) & 
                                 (Files.FF == True))
        query_output = db.search(fn_ff_query_by_energy)    
        files_FF = get_file_paths(query_output, root_path, 
                                  use_subfolders=True,
                                  only_existing_files=False)    
            
        files_for_sample_subdict['tomos'] = files_by_zp
        files_for_sample_subdict['ff'] = files_FF
        many_tomos_experiment_files[date_sample_energie] = files_for_sample_subdict

    
    #files_for_sample[]
        
        
   
    prettyprinter.pprint(many_tomos_experiment_files)
    
    
    
    
    
    
    """
    
    
    
    #root_path = os.path.dirname(os.path.abspath(index_fn))
    #files = get_file_paths(query_output, root_path, use_subfolders=False,
    #                       only_existing_files=False)
     

    """    
    
    """
    files = search_and_get_file_paths(txm_txt_script, query_impl,
                                      use_existing_db=True,
                                      use_subfolders=True, 
                                      only_existing_files=False)
    """             
        

    """
    #for i in files:
    #    print(i)
    #    print("\n")  
    """    
        
        
 
        
        
        
        
        
        
        
        
        
  


        
        
        
        
        
        
   
    """


    #prettyprinter.pprint(collected_images)
    
   
    
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
        
    
    found2 = db.search(Files.zpz < 1)
    found3 = db.search(Files.zp.exists())
    #print(found3)
    
    res2 = sorted(found2, key=itemgetter('zpz'), reverse=False)
    zpz_all_files = [] 
    for entry in res2:
        pass
        #print(entry["zpz"])
    
    
    for entry in result:
        pass

    db.close()
    
    #with open('db.json') as data_file:
    #    data = json.load(data_file)
    #print(data)
    """

if __name__ == "__main__":
    main()

