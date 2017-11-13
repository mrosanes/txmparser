import os
import copy
import pprint

# Problems can exist with FF, sample name, repetition number; because they
# are not motors of the microscope


class ParserTXMScript:

    def __init__(self):
        self.date = None
        self.sample = "sample0"
        self.energy = None
        self.angle = None
        self.zpz = None
        self.FF = False
        self.repetition = 0
        
    def parse_script(self, txm_txt_script):

        f = open(txm_txt_script, 'r')

        collected_images = []
        parameters = {}
        
        energy = 0
        zP = 0
        angle = 0
        repetition = 0
        modified = False
        
        lines = f.readlines()
        for i, line in enumerate(lines):
            s1 = "moveto energy"
            s2 = "moveto ZPz"
            s3 = "moveto T"

            if "moveto energy" in line:
                modified = True
                repetition = 0
                word_list = line.split()
                self.energy = round(float(word_list[-1]), 1)
                parameters['energy'] = self.energy
                modified = True
                
            if "moveto T" in line:
                modified = True
                repetition = 0
                word_list = line.split()
                self.angle = round(float(word_list[-1]), 1)
                parameters['angle'] = self.angle

            if "moveto ZPz" in line:
                modified = True
                repetition = 0
                word_list = line.split()
                self.zpz = round(float(word_list[-1]), 1)
                parameters['zpz'] = self.zpz
                
            if "collect" in line:
                if modified == False:
                    repetition += 1
                parameters['repetition'] = repetition
                
                word_list = line.split()
                filename = word_list[-1]
                parameters['filename'] = filename
            
                if "_FF" in filename:
                    self.FF = True
                    parameters['FF'] = self.FF
                else:
                    self.FF = False
                    parameters['FF'] = self.FF
                
                try:
                    date = float(os.path.basename(filename).split('_')[0])
                    if (len(date) == 4 or len(date) == 6 or len(date) == 8):
                        date = os.path.basename(filename).split('_')[0]
                        parameters['date'] = date
                        self.sample = os.path.basename(
                            filename).split('_')[1]
                    else:
                        self.sample = os.path.basename(
                            filename).split('_')[0]
                except:
                    self.sample = os.path.basename(
                        filename).split('_')[0]
                parameters['sample'] = self.sample
                
                store_parameters = copy.deepcopy(parameters)
                #print(store_parameters)
                collected_images.append(store_parameters)
                modified = False
            
        return collected_images
            
        
def main():

    parser = ParserTXMScript()
    collected_images = parser.pars_script("many.txt")
    prettyprinter = pprint.PrettyPrinter(indent=4)
    prettyprinter.pprint(collected_images)

    
    
if __name__ == "__main__":
    main()
