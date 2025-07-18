import mne
import matplotlib
data_path= input("Enter the path of '.set' file\n>> ")

is_raw=False
is_epoch=False
epoch_ready=False


try:
    data = mne.read_epochs_eeglab(data_path)
    is_epoch=True
except:
    data =mne.io.read_raw_eeglab(data_path)
    is_raw=True

while True:
    if is_raw==False and epoch_ready==False:
        print("-----------------------------------------------------\nTo import new EEGLAB data enter 'import'\n To plot data enter 'plot' \n To plot power spectral density enter 'psd'\n To plot data ERP enter 'erp'\n To exit enter 'exit'\n-----------------------------------------------------")
        todo=input(">> ")
    if is_raw==True and epoch_ready==False:
        print("-----------------------------------------------------\nTo import new EEGLAB data enter 'import'\n To plot data enter 'plot' \n To plot power spectral density enter 'psd'\n To plot data ERP enter 'erp'\n To exit enter 'exit'\nTo turn annotations into epochs enter 'ae'\n-----------------------------------------------------")
        todo=input(">> ")
    if is_raw==True and epoch_ready==True:
        print("-----------------------------------------------------\nTo import new EEGLAB data enter 'import'\n To plot data enter 'plot' \n To plot power spectral density enter 'psd'\n To plot data ERP enter 'erp'\n To exit enter 'exit'\n\n To plot EPOCHED DATA enter 'plot-e' \n To plot EPOCHED DATA power spectral density enter 'psd-e'\n To plot EPOCHED DATA ERP enter 'erp-e'\n-----------------------------------------------------")
        todo=input(">> ")




    if todo =="import":
        data_path= input("Enter the path of '.set' file\n>>")
        is_raw=False
        is_epoch=False
        epoch_ready=False
        try:
            data = mne.read_epochs_eeglab(data_path)
            is_epoch=True
        except:
            data =mne.io.read_raw_eeglab(data_path)
            is_raw=True
    if todo=="ae":
        events_from_annot, event_dict = mne.events_from_annotations(data)
        epochs = mne.Epochs(data,events_from_annot, event_dict)
        epoch_ready=True

    if todo=="plot-e":
        epochs.plot(block=True)
    if todo=="psd-e":
        epochs.plot_psd(spatial_colors=True)
    if todo=="erp-e":
        epochs.average().plot(spatial_colors=True, gfp=True)
    if todo=="plot":
        data.plot(block=True)
    if todo=="psd":
        data.plot_psd(spatial_colors=True)
    if todo=="erp":
        if is_epoch==True:
            data.average().plot(spatial_colors=True, gfp=True)
        else:
            print("Data must be epoch data")
    if todo=="exit":
        break
