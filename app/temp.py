""" Code from filtrack that worked
    kept here for reference
"""


     #filenames[:] = [f for f in filenames if  not f.startswith('__')]
 97 
 98         #for subfolder in subfolders:
 99             #print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
100             #filenames[:] = [f for f in filenames if  re.findSall('test', f, flags=re.IGN    ORECASE)]   
             #pass

            #print('FILE INSIDE ' + folderName + ': '+ filename)
            full_file_path = shlex.quote(os.path.join(root, filename))
            print(f"root: {root}\nfilename: {filename}"
            #print(full_file_path)
            if os.path.isfile(full_file_path):
                filehash = hm.hash_file(full_file_path)
                timestamp = getmoddate(full_file_path)
                record = {'filename':filename, 
                          'filepath':full_file_path,
                          'filehash':filehash,
                          'timestamp':timestamp}
                check_record = mydb.show_duplicate_records(table, 'filehash', filehash)
                if is_rec_modified(full_file_path):
                        mydb.update_record(full_file_path):
                elif len(check_record) == 0:
                        mydb.add_record(table, record)
                else:
                    pass

                    #for f_name, f_path, f_hash in check_record:
                    #    print(f"{f_name}\n{f_path}\n{f_hash}\n")
                
                #if  record_ck not in check_record:
                    #print(check_record)
            #print('-' * 70)
            #print(f'{full_file_path:70}\n{filename:25}\n{filehash:50}\n')
            
    #print('-' * 70)
            #print(folderName)
    all_records = mydb.show_all_records(table)
    for my_record in all_records:
      #  print(my_record[0], my_record[1], my_record[2],my_record[3])

