import argparse

class Test_options():
    def __init__(self):
        parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        self.initialize(parser)
    def initialize(self,parser):
        parser.add_argument('--dataroot', required=True,help='path to test data. For linear regression, it is the path to training data.')
        parser.add_argument('--dataroot1',help='path to test data for linear regression.')
        parser.add_argument('--instrument_data', default='', help='path to test dataset only for linear regression')
        parser.add_argument('--name',required=True,help='name of the model saved in ./checkpoints/ if use cnn. experiment name if use linear regression')
        parser.add_argument('--model',default='cnn',help='name of model to use. cnn | linear_regression')
        parser.add_argument('--leadtime', type=int, default=1, help='leadtime of model')
        parser.add_argument('--num_input_time_steps', type=int, default=1, help='the number of input time steps in the predictor')
        parser.add_argument('--startdate',required=True,help='start date of data as yyyy-mm-dd')
        parser.add_argument('--enddate',required=True,help='end date of data as yyyy-mm-dd')
        parser.add_argument('--pca',action='store_true',help='use pca')
        parser.add_argument('--n_components',type=int, default=32, help='the number of components to use for PCA')
        parser.add_argument('--dataset', default='observations', help="observations | CNRM | MPI. Training dataset for linear regression.")
        parser.add_argument('--data_format',default='spatial', help = "'spatial' or 'flatten'. 'spatial' preserves the lat/lon dimensions and returns an array of shape (num_samples, num_input_time_steps, lat, lon).  'flatten' returns an array of shape (num_samples, num_input_time_steps*lat*lon)") 
        parser.add_argument('--batch_size',type=int, default=10, help='training batch size')
        parser.add_argument('--classification', action='store_true', help='use classification')
        parser.add_argument('--threshold', type=float, default=1.5, help='threshold of Nino 3.4 index as El Nino')
        parser.add_argument('--test_start',default='',help='test start date only for linear regression')
        parser.add_argument('--test_end',default='',help='test end date only for linear regression')
        parser.add_argument('--lat_slice',default=None, help='the slice of latitudes to use')
        parser.add_argument('--lon_slice',default=None, help='the slice of longitudes to use')
        parser.add_argument('--variable_name', default='', help='variable name of test data. For linear regression, it is the training data.')
        parser.add_argument('--variable_name_ref', default='sst', help='variable name of test data for linear regression.')
        parser.add_argument('--compare_ground_truth', action='store_true', help='whether compare the prediction with ground truth.')
        
        
        self.parser=parser
    def parse(self):
        return self.parser.parse_args()
