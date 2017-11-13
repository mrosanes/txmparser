import os
import copy
import pprint

# Problems can exist with FF, sample name, repetition number; because they
# are not motors of the microscope


class ParserTXMScript:

    def __init__(self):
        self.collected_files = []
        self.parameters = {}
        self.date = None
        self.sample = "sample0"
        self.energy = -1
        self.angle = -1000
        self.zpz = -1
        self.FF = False
        self.repetition = 0
        self.first_repetition = True
        self.extension = None
        self.filename = None
        
    def parse_energy(self, line):
        # If a parameter is modified, the repetitions must be reset
        self.first_repetition = True
        self.repetition = 0
        word_list = line.split()
        self.energy = round(float(word_list[-1]), 1)
        self.parameters['energy'] = self.energy
                
    def parse_angle(self, line):
        # If a parameter is modified, the repetitions must be reset
        self.first_repetition = True
        self.repetition = 0
        word_list = line.split()
        self.angle = round(float(word_list[-1]), 1)
        self.parameters['angle'] = self.angle
        
    def parse_zpz(self, line):
        # If a parameter is modified, the repetitions must be reset
        self.first_repetition = True
        self.repetition = 0
        word_list = line.split()
        self.zpz = round(float(word_list[-1]), 1)
        self.parameters['zpz'] = self.zpz
    
    def is_FF(self):
        if "_FF" in self.filename:
            # If a parameter is modified, the repetitions must be reset
            if self.FF == False:
                self.first_repetition = True
            self.FF = True
            self.parameters['FF'] = self.FF
        else:
            # If a parameter is modified, the repetitions must be reset
            if self.FF == True:
                self.first_repetition = True
            self.FF = False
            self.parameters['FF'] = self.FF
        
    def parse_sample_and_date(self):
        try:
            date_str = self.filename.split('_')[0]
            new_date = int(date_str)
            # If a parameter is modified, the repetitions must be reset
            if new_date != self.date:
                self.first_repetition = True
            self.date = new_date
            if (len(date_str) == 4 or 
                len(date_str) == 6 or 
                len(date_str) == 8):
                self.parameters['date'] = self.date
                new_sample = self.filename.split('_')[1]
                # If a parameter is modified, the repetitions must be reset
                if new_sample != self.sample:
                    self.first_repetition = True
                self.sample = new_sample                    
            else:
                new_sample = self.filename.split('_')[0]
                # If a parameter is modified, the repetitions must be reset
                if new_sample != self.sample:
                    self.first_repetition = True
                self.sample = new_sample
        except:
            self.parameters.pop('date', None)
            self.sample = self.filename.split('_')[0]
        self.parameters['sample'] = self.sample
        
    def parse_extension(self):
        self.extension = os.path.splitext(self.filename)[1]
        self.parameters['extension'] = self.extension        
        
    def parse_collect(self, line):
        if self.first_repetition == False:
            self.repetition += 1
        self.parameters['repetition'] = self.repetition
        
        word_list = line.split()
        self.filename = word_list[-1]
        self.parameters['filename'] = self.filename
    
        self.is_FF()
        self.parse_extension()
        self.parse_sample_and_date()

        store_parameters = copy.deepcopy(self.parameters)
        #print(store_parameters)
        self.collected_files.append(store_parameters)
        self.first_repetition = False
    
    def parse_script(self, txm_txt_script):
        f = open(txm_txt_script, 'r')
        
        lines = f.readlines()
        for i, line in enumerate(lines):
            s1 = "moveto energy"
            s2 = "moveto ZPz"
            s3 = "moveto T"

            if "moveto energy" in line:
                self.parse_energy(line)
                
            if "moveto T" in line:
                self.parse_angle(line)
                
            if "moveto ZPz" in line:
                self.parse_zpz(line)
                
            if "collect" in line:
                self.parse_collect(line)
                
        return self.collected_files
                
        
def main():

    parser = ParserTXMScript()
    collected_images = parser.parse_script("many.txt")
    prettyprinter = pprint.PrettyPrinter(indent=4)
    prettyprinter.pprint(collected_images)

    
    
if __name__ == "__main__":
    main()
