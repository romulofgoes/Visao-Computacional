def aux_zera_ao_redor(fshift, i, j):
    if(fshift[i+1][j]): fshift[i+1][j] = 0
    if(fshift[i][j+1]): fshift[i][j+1] = 0
    if(fshift[i+1][[j+1]]): fshift[i+1][j+1] = 0
    if(fshift[i-1][j]): fshift[i-1][j] = 0
    if(fshift[i][j-1]): fshift[i][j-1] = 0
    if(fshift[i-1][j-1]): fshift[i-1][j-1] = 0
    if(fshift[i+1][j-1]): fshift[i+1][j-1] = 0
    if(fshift[i-1][j+1]): fshift[i-1][j+1] = 0
    return fshift


def mask(img_src, fshift, limite_de_centro=40, val_min=210, val_max=255):
    center_limit = limite_de_centro

    img_center = [img_src.shape[0]/2, img_src.shape[1]/2]

    img_limits = [[img_center[0]-center_limit, img_center[0]+center_limit], [img_center[1]-center_limit, img_center[1]+center_limit]]

    for i in range(img_src.shape[0]):
        for j in range(img_src.shape[1]):
            if((i < img_limits[0][0] or i > img_limits[0][1]) or (j < img_limits[1][0] or j > img_limits[1][1])):
                if(val_min<int(img_src[i][j]) <= val_max):
                    fshift[i][j] = 0 
                    aux_zera_ao_redor(fshift, i, j)
                    
    return fshift