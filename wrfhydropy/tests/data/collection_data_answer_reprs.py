ensemble_answer_reprs = {
    'v5.1.0': {
        '*/*CHRTOUT_DOMAIN1':
        "<xarray.Dataset>\nDimensions:     (feature_id: 185, member: 3, time: 2)\nCoordinates:\n  * feature_id  (feature_id) int32 6226932 6226946 6228408 ... 6226970 6226924\n    latitude    (feature_id) float32 41.476772 41.472435 ... 41.462833 41.47584\n    longitude   (feature_id) float32 -73.76406 -73.73539 ... -73.729996\n  * time        (time) datetime64[ns] 2011-08-26T01:00:00 2011-08-26T02:00:00\n  * member      (member) int64 0 1 2\nData variables:\n    crs         (member, time) |S1 b'' b'' b'' b'' b'' b''\n    order       (member, time, feature_id) int32 2 2 2 2 2 2 2 ... 1 1 1 1 1 1 1\n    elevation   (member, time, feature_id) float32 207.02 215.14 ... 222.33\n    streamflow  (member, time, feature_id) float32 0.14420484 ... 0.0008179697\n    nudge       (member, time, feature_id) float32 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    q_lateral   (member, time, feature_id) float32 0.0037602568 ... 0.0\n    velocity    (member, time, feature_id) float32 0.14997235 ... 0.00074039085\n    Head        (member, time, feature_id) float32 0.24364558 ... 0.37814376\nAttributes:\n    featureType:        timeSeries\n    proj4:              +proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=3...\n    station_dimension:  feature_id\n    Conventions:        CF-1.6",
        '*/*LAKEOUT_DOMAIN1':
        "<xarray.Dataset>\nDimensions:         (feature_id: 1, member: 3, time: 2)\nCoordinates:\n  * feature_id      (feature_id) int32 6228110\n    latitude        (feature_id) float32 41.424545\n    longitude       (feature_id) float32 -73.70292\n  * time            (time) datetime64[ns] 2011-08-26T01:00:00 2011-08-26T02:00:00\n  * member          (member) int64 0 1 2\nData variables:\n    crs             (member, time) |S1 b'' b'' b'' b'' b'' b''\n    water_sfc_elev  (member, time, feature_id) float32 156.59833 ... 156.59833\n    inflow          (member, time, feature_id) float32 1.4711169 ... 1.4670238\n    outflow         (member, time, feature_id) float32 1.3938106 ... 1.3938106\nAttributes:\n    featureType:        timeSeries\n    proj4:              +proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=3...\n    station_dimension:  lake_id\n    Conventions:        CF-1.6",
        '*/*CHANOBS_DOMAIN1':
        "<xarray.Dataset>\nDimensions:     (feature_id: 4, member: 3, time: 2)\nCoordinates:\n  * feature_id  (feature_id) int32 6226948 6226964 6227008 6227150\n    latitude    (feature_id) float32 41.470795 41.473614 41.449814 41.40192\n    longitude   (feature_id) float32 -73.76059 -73.69085 -73.73565 -73.68741\n  * time        (time) datetime64[ns] 2011-08-26T01:00:00 2011-08-26T02:00:00\n  * member      (member) int64 0 1 2\nData variables:\n    crs         (member, time) |S1 b'' b'' b'' b'' b'' b''\n    order       (member, time, feature_id) int32 3 2 4 4 3 2 4 ... 2 4 4 3 2 4 4\n    elevation   (member, time, feature_id) float32 180.48 183.15 ... 147.61\n    streamflow  (member, time, feature_id) float32 0.4666675 ... 1.4402199\nAttributes:\n    featureType:        timeSeries\n    proj4:              +proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=3...\n    station_dimension:  feature_id\n    Conventions:        CF-1.6",
        '*/*GWOUT_DOMAIN1':
        '<xarray.Dataset>\nDimensions:     (feature_id: 185, member: 3, time: 2)\nCoordinates:\n  * feature_id  (feature_id) int32 6212272 6212276 6212914 ... 6228424 6228442\n  * time        (time) datetime64[ns] 2011-08-26T01:00:00 2011-08-26T02:00:00\n  * member      (member) int64 0 1 2\nData variables:\n    inflow      (member, time, feature_id) float32 0.011821471 ... 0.065097235\n    outflow     (member, time, feature_id) float32 0.011858283 ... 0.06498866\n    depth       (member, time, feature_id) float32 0.0068849023 ... 0.050821777\nAttributes:\n    featureType:        timeSeries\n    station_dimension:  gw_id\n    Conventions:        CF-1.6',
        '*/*RTOUT_DOMAIN1': "<xarray.Dataset>\nDimensions:       (member: 3, soil_layers_stag: 4, time: 2, x: 60, y: 64)\nCoordinates:\n  * x             (x) float64 1.842e+06 1.842e+06 ... 1.857e+06 1.857e+06\n  * y             (y) float64 4.211e+05 4.214e+05 ... 4.366e+05 4.369e+05\n  * time          (time) datetime64[ns] 2011-08-26T01:00:00 2011-08-26T02:00:00\n  * member        (member) int64 0 1 2\nDimensions without coordinates: soil_layers_stag\nData variables:\n    crs           (member, time) |S1 b'' b'' b'' b'' b'' b''\n    zwattablrt    (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    sfcheadsubrt  (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    QSTRMVOLRT    (member, time, y, x) float32 0.0 142.5398 142.5398 ... 0.0 0.0\n    QBDRYRT       (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    SOIL_M        (member, time, y, soil_layers_stag, x) float32 0.3480787 ... 0.4255304\nAttributes:\n    Conventions:  CF-1.6\n    proj4:        +proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=30.0 +l...",
        '*/*LDASOUT_DOMAIN1': "<xarray.Dataset>\nDimensions:      (member: 3, snow_layers: 3, soil_layers_stag: 4, time: 3, vis_nir: 2, x: 15, y: 16)\nCoordinates:\n  * x            (x) float64 1.843e+06 1.844e+06 ... 1.856e+06 1.857e+06\n  * y            (y) float64 -4.365e+05 -4.355e+05 ... -4.225e+05 -4.215e+05\n  * time         (time) datetime64[ns] 2011-08-26 ... 2011-08-26T02:00:00\n  * member       (member) int64 0 1 2\nDimensions without coordinates: snow_layers, soil_layers_stag, vis_nir\nData variables:\n    crs          (member, time) |S1 b'' b'' b'' b'' b'' b'' b'' b'' b''\n    IVGTYP       (member, time, y, x) float32 11.0 11.0 11.0 ... 11.0 11.0 11.0\n    ISLTYP       (member, time, y, x) float32 3.0 3.0 3.0 3.0 ... 3.0 3.0 3.0\n    FVEG         (member, time, y, x) float32 nan nan ... 0.98999995 0.98999995\n    LAI          (member, time, y, x) float32 2.761096 2.761096 ... 2.755068\n    SAI          (member, time, y, x) float32 1.3161645 1.3161645 ... 1.3172604\n    SWFORC       (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    COSZ         (member, time, y, x) float32 nan nan ... -0.27193752\n    LWFORC       (member, time, y, x) float32 nan nan ... 379.01874 379.04007\n    RAINRATE     (member, time, y, x) float32 nan nan ... 1.0471035e-06\n    EMISS        (member, time, y, x) float32 nan nan ... 0.99969137 0.99969137\n    FSA          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    FIRA         (member, time, y, x) float32 nan nan nan ... 42.589893 42.89331\n    GRDFLX       (member, time, y, x) float32 nan nan ... -16.265245 -16.16816\n    HFX          (member, time, y, x) float32 nan nan ... -34.180138 -34.36277\n    LH           (member, time, y, x) float32 nan nan nan ... 7.8560576 7.638099\n    ECAN         (member, time, y, x) float32 nan nan ... 5.2672686e-07\n    EDIR         (member, time, y, x) float32 nan nan ... 2.419544e-06\n    ALBEDO       (member, time, y, x) float32 nan nan nan nan ... nan nan nan\n    ETRAN        (member, time, y, x) float32 nan nan ... 9.63116e-08\n    UGDRNOFF     (member, time, y, x) float32 560.2294 615.589 ... 903.26166\n    SFCRNOFF     (member, time, y, x) float32 186.69469 262.8587 ... 550.79767\n    CANLIQ       (member, time, y, x) float32 0.0 0.0 ... 6.792904e-05\n    CANICE       (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    ZWT          (member, time, y, x) float32 2.5 2.5 2.5 2.5 ... 2.5 2.5 2.5\n    WA           (member, time, y, x) float32 4900.0 4900.0 ... 4900.0 4900.0\n    WT           (member, time, y, x) float32 4900.0 4900.0 ... 4900.0 4900.0\n    ACCPRCP      (member, time, y, x) float32 1682.4382 1684.4056 ... 1631.8362\n    ACCECAN      (member, time, y, x) float32 131.5012 130.83821 ... 127.482864\n    ACCEDIR      (member, time, y, x) float32 132.10272 149.89125 ... 145.20123\n    ACCETRAN     (member, time, y, x) float32 467.5134 467.78235 ... 551.33655\n    SAV          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    TR           (member, time, y, x) float32 nan nan ... 0.23732407 0.24178064\n    EVC          (member, time, y, x) float32 nan nan ... 1.5555513 1.3222951\n    IRC          (member, time, y, x) float32 nan nan nan ... 38.122753 38.47299\n    SHC          (member, time, y, x) float32 nan nan ... -39.913727 -40.035465\n    IRG          (member, time, y, x) float32 nan nan nan ... 4.0898957 4.040604\n    SHG          (member, time, y, x) float32 nan nan nan ... 5.828075 5.767493\n    EVG          (member, time, y, x) float32 nan nan ... 6.1071024 6.1184664\n    GHV          (member, time, y, x) float32 nan nan ... -16.026398 -15.927674\n    SAG          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    IRB          (member, time, y, x) float32 nan nan nan ... 41.814125 42.01206\n    SHB          (member, time, y, x) float32 nan nan ... -3.6204343 -3.7120464\n    EVB          (member, time, y, x) float32 nan nan ... 1.7151028 1.6741753\n    GHB          (member, time, y, x) float32 nan nan ... -39.91099 -39.97602\n    TRAD         (member, time, y, x) float32 nan nan ... 293.65338 293.70993\n    TG           (member, time, y, x) float32 295.7495 295.73914 ... 294.6739\n    TV           (member, time, y, x) float32 295.35333 295.34418 ... 294.09592\n    TAH          (member, time, y, x) float32 295.45782 295.44968 ... 294.2122\n    TGV          (member, time, y, x) float32 nan nan ... 294.63745 294.68292\n    TGB          (member, time, y, x) float32 nan nan ... 293.74115 293.78033\n    T2MV         (member, time, y, x) float32 nan nan nan ... 294.37836 294.4318\n    T2MB         (member, time, y, x) float32 nan nan nan ... 294.2389 294.2854\n    Q2MV         (member, time, y, x) float32 nan nan ... 0.01531457 0.015344455\n    Q2MB         (member, time, y, x) float32 nan nan ... 0.01530286 0.015335441\n    EAH          (member, time, y, x) float32 2420.3884 2421.9019 ... 2375.697\n    FWET         (member, time, y, x) float32 0.0 0.0 ... 0.003021453\n    ZSNSO_SN     (member, time, y, snow_layers, x) float32 nan nan ... nan nan\n    SNICE        (member, time, y, snow_layers, x) float32 0.0 0.0 ... 0.0 0.0\n    SNLIQ        (member, time, y, snow_layers, x) float32 0.0 0.0 ... 0.0 0.0\n    SOIL_T       (member, time, y, soil_layers_stag, x) float32 295.86893 ... 291.4641\n    SOIL_W       (member, time, y, soil_layers_stag, x) float32 0.30749175 ... 0.3486558\n    SNOW_T       (member, time, y, snow_layers, x) float32 0.0 0.0 ... 0.0 0.0\n    SOIL_M       (member, time, y, soil_layers_stag, x) float32 0.30749175 ... 0.3486558\n    SNOWH        (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    SNEQV        (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    QSNOW        (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    ISNOW        (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    FSNO         (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    ACSNOW       (member, time, y, x) float32 0.054744314 ... 0.05116239\n    ACSNOM       (member, time, y, x) float32 201.04697 201.5238 ... 191.20047\n    CM           (member, time, y, x) float32 0.016443286 ... 0.015046084\n    CH           (member, time, y, x) float32 0.058478564 ... 0.05410032\n    CHV          (member, time, y, x) float32 nan nan ... 0.05393088 0.05461069\n    CHB          (member, time, y, x) float32 nan nan ... 0.0035740503\n    CHLEAF       (member, time, y, x) float32 nan nan ... 0.30793443 0.30909222\n    CHUC         (member, time, y, x) float32 nan nan ... 0.010562936\n    CHV2         (member, time, y, x) float32 nan nan ... 0.1345794 0.13611871\n    CHB2         (member, time, y, x) float32 nan nan ... 0.006336383\n    LFMASS       (member, time, y, x) float32 60.62929 60.95988 ... 61.898296\n    RTMASS       (member, time, y, x) float32 500.0 500.0 500.0 ... 500.0 500.0\n    STMASS       (member, time, y, x) float32 161.67812 162.5597 ... 165.06213\n    WOOD         (member, time, y, x) float32 500.0 500.0 500.0 ... 500.0 500.0\n    STBLCP       (member, time, y, x) float32 1000.0 1000.0 ... 1000.0 1000.0\n    FASTCP       (member, time, y, x) float32 1000.0 1000.0 ... 1000.0 1000.0\n    NEE          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    GPP          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    NPP          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    PSN          (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    APAR         (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    ACCET        (member, time, y, x) float32 731.1173 748.51184 ... 824.0206\n    CANWAT       (member, time, y, x) float32 0.0 0.0 ... 6.792904e-05\n    SOILICE      (member, time, y, x) float32 nan nan nan nan ... 0.0 0.0 0.0\n    SOILSAT_TOP  (member, time, y, x) float32 nan nan ... 0.6403721 0.6404696\n    SOILSAT      (member, time, y, x) float32 nan nan ... 0.67061496 0.67420465\n    SNOWT_AVG    (member, time, y, x) float32 nan nan nan nan ... nan nan nan\n    ALBSND       (member, time, y, vis_nir, x) float32 nan nan nan ... 0.0 0.0\n    ALBSNI       (member, time, y, vis_nir, x) float32 nan nan nan ... 0.0 0.0\nAttributes:\n    Conventions:  CF-1.6\n    proj4:        +proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=30.0 +l...",
        '*/*LSMOUT_DOMAIN': "<xarray.Dataset>\nDimensions:    (member: 3, time: 2, x: 15, y: 16)\nCoordinates:\n  * x          (x) float64 1.843e+06 1.844e+06 1.845e+06 ... 1.856e+06 1.857e+06\n  * y          (y) float64 -4.365e+05 -4.355e+05 ... -4.225e+05 -4.215e+05\n  * time       (time) datetime64[ns] 2011-08-26T01:00:00 2011-08-26T02:00:00\n  * member     (member) int64 0 1 2\nData variables:\n    crs        (member, time) |S1 b'' b'' b'' b'' b'' b''\n    stc1       (member, time, y, x) float32 295.36743 295.35336 ... 294.891\n    smc1       (member, time, y, x) float32 0.3064709 0.30986938 ... 0.31681895\n    sh2ox1     (member, time, y, x) float32 0.3064709 0.30986938 ... 0.31681895\n    stc2       (member, time, y, x) float32 293.64014 293.60013 ... 293.51782\n    smc2       (member, time, y, x) float32 0.31128648 0.31444216 ... 0.3187387\n    sh2ox2     (member, time, y, x) float32 0.31128648 0.31444216 ... 0.3187387\n    stc3       (member, time, y, x) float32 292.67325 292.63126 ... 292.5082\n    smc3       (member, time, y, x) float32 0.3202931 0.32370606 ... 0.32347515\n    sh2ox3     (member, time, y, x) float32 0.3202931 0.32370606 ... 0.32347515\n    stc4       (member, time, y, x) float32 291.7632 291.72418 ... 291.4641\n    smc4       (member, time, y, x) float32 0.35623673 0.36004874 ... 0.3486558\n    sh2ox4     (member, time, y, x) float32 0.35623673 0.36004874 ... 0.3486558\n    infxsrt    (member, time, y, x) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0 0.0\n    sfcheadrt  (member, time, y, x) float32 0.0 0.008182592 0.0 ... 0.0 0.0 0.0\nAttributes:\n    Conventions:  CF-1.6\n    proj4:        +proj=lcc +units=m +a=6370000.0 +b=6370000.0 +lat_1=30.0 +l...",
        '*/HYDRO_RST.*_DOMAIN1':
        '<xarray.Dataset>\nDimensions:       (ix: 15, ixrt: 60, iy: 16, iyrt: 64, lakes: 1, links: 185, member: 3, time: 3)\nCoordinates:\n  * time          (time) datetime64[ns] 2011-08-26 ... 2011-08-26T02:00:00\n  * member        (member) int64 0 1 2\nDimensions without coordinates: ix, ixrt, iy, iyrt, lakes, links\nData variables:\n    stc1          (member, time, iy, ix) float32 295.86893 295.8609 ... 294.891\n    smc1          (member, time, iy, ix) float32 0.30749175 ... 0.31681895\n    sh2ox1        (member, time, iy, ix) float32 0.30749175 ... 0.31681895\n    stc2          (member, time, iy, ix) float32 293.5919 ... 293.51782\n    smc2          (member, time, iy, ix) float32 0.31137833 ... 0.3187387\n    sh2ox2        (member, time, iy, ix) float32 0.31137833 ... 0.3187387\n    stc3          (member, time, iy, ix) float32 292.6696 292.62756 ... 292.5082\n    smc3          (member, time, iy, ix) float32 0.3202184 ... 0.32347515\n    sh2ox3        (member, time, iy, ix) float32 0.3202184 ... 0.32347515\n    stc4          (member, time, iy, ix) float32 291.76456 ... 291.4641\n    smc4          (member, time, iy, ix) float32 0.35623375 ... 0.3486558\n    sh2ox4        (member, time, iy, ix) float32 0.35623375 ... 0.3486558\n    infxsrt       (member, time, iy, ix) float32 0.0 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    soldrain      (member, time, iy, ix) float32 0.068881854 ... 0.039847232\n    sfcheadrt     (member, time, iy, ix) float32 0.0 0.001411202 0.0 ... 0.0 0.0\n    QBDRYRT       (member, time, iyrt, ixrt) float32 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    infxswgt      (member, time, iyrt, ixrt) float32 0.0625 0.0625 ... 0.0625\n    sfcheadsubrt  (member, time, iyrt, ixrt) float32 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    sh2owgt1      (member, time, iyrt, ixrt) float32 1.1357642 ... 1.2252156\n    sh2owgt2      (member, time, iyrt, ixrt) float32 1.2128946 ... 1.2752639\n    sh2owgt3      (member, time, iyrt, ixrt) float32 1.2872615 ... 1.3617415\n    sh2owgt4      (member, time, iyrt, ixrt) float32 1.2076954 ... 1.2204885\n    qstrmvolrt    (member, time, iyrt, ixrt) float32 0.0 142.5398 ... 0.0 0.0\n    hlink         (member, time, links) float32 0.032560024 ... 2.4060745\n    qlink1        (member, time, links) float32 0.0331037 ... 0.32772997\n    qlink2        (member, time, links) float32 0.0331037 ... 0.32772997\n    resht         (member, time, lakes) float32 156.59833 ... 156.59833\n    qlakeo        (member, time, lakes) float32 1.3938106 ... 1.3938106\n    qlakei        (member, time, lakes) float32 1.47184 1.4711169 ... 1.4670238\n    lake_inflort  (member, time, iyrt, ixrt) float32 0.0 0.0 0.0 ... 0.0 0.0 0.0\n    z_gwsubbas    (member, time, links) float32 6.9443486e-06 ... 5.0821778e-05',
        '*/RESTART.*_DOMAIN1':
        "<xarray.Dataset>\nDimensions:      (member: 3, snow_layers: 3, soil_layers_stag: 4, sosn_layers: 7, south_north: 16, time: 3, west_east: 15)\nCoordinates:\n  * time         (time) object b'2011-08-26_00:00:00' ... b'2011-08-26_02:00:00'\n  * member       (member) int64 0 1 2\nDimensions without coordinates: snow_layers, soil_layers_stag, sosn_layers, south_north, west_east\nData variables:\n    SOIL_T       (member, time, south_north, soil_layers_stag, west_east) float32 295.86893 ... 291.4641\n    SNOW_T       (member, time, south_north, snow_layers, west_east) float32 0.0 ... 0.0\n    SMC          (member, time, south_north, soil_layers_stag, west_east) float32 0.30749175 ... 0.3486558\n    SH2O         (member, time, south_north, soil_layers_stag, west_east) float32 0.30749175 ... 0.3486558\n    ZSNSO        (member, time, south_north, sosn_layers, west_east) float32 0.0 ... -2.0\n    SNICE        (member, time, south_north, snow_layers, west_east) float32 0.0 ... 0.0\n    SNLIQ        (member, time, south_north, snow_layers, west_east) float32 0.0 ... 0.0\n    QSNOW        (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    FWET         (member, time, south_north, west_east) float32 0.0 ... 0.003021453\n    SNEQVO       (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    EAH          (member, time, south_north, west_east) float32 2420.3884 ... 2375.697\n    TAH          (member, time, south_north, west_east) float32 295.45782 ... 294.2122\n    ALBOLD       (member, time, south_north, west_east) float32 0.65 ... 0.65\n    CM           (member, time, south_north, west_east) float32 0.016443286 ... 0.015046084\n    CH           (member, time, south_north, west_east) float32 0.058478564 ... 0.05410032\n    ISNOW        (member, time, south_north, west_east) int32 0 0 0 0 ... 0 0 0\n    CANLIQ       (member, time, south_north, west_east) float32 0.0 ... 6.792904e-05\n    CANICE       (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    SNEQV        (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    SNOWH        (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    TV           (member, time, south_north, west_east) float32 295.35333 ... 294.09592\n    TG           (member, time, south_north, west_east) float32 295.7495 ... 294.6739\n    ZWT          (member, time, south_north, west_east) float32 2.5 2.5 ... 2.5\n    WA           (member, time, south_north, west_east) float32 4900.0 ... 4900.0\n    WT           (member, time, south_north, west_east) float32 4900.0 ... 4900.0\n    WSLAKE       (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    LFMASS       (member, time, south_north, west_east) float32 60.62929 ... 61.898296\n    RTMASS       (member, time, south_north, west_east) float32 500.0 ... 500.0\n    STMASS       (member, time, south_north, west_east) float32 161.67812 ... 165.06213\n    WOOD         (member, time, south_north, west_east) float32 500.0 ... 500.0\n    STBLCP       (member, time, south_north, west_east) float32 1000.0 ... 1000.0\n    FASTCP       (member, time, south_north, west_east) float32 1000.0 ... 1000.0\n    LAI          (member, time, south_north, west_east) float32 2.761096 ... 2.755068\n    SAI          (member, time, south_north, west_east) float32 1.3161645 ... 1.3172604\n    VEGFRA       (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    GVFMIN       (member, time, south_north, west_east) float32 17.471191 ... 19.255075\n    GVFMAX       (member, time, south_north, west_east) float32 98.37664 ... 98.99999\n    ACMELT       (member, time, south_north, west_east) float32 201.04697 ... 191.20047\n    ACSNOW       (member, time, south_north, west_east) float32 0.054744314 ... 0.05116239\n    TAUSS        (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    QSFC         (member, time, south_north, west_east) float32 0.01662413 ... 0.015470233\n    SFCRUNOFF    (member, time, south_north, west_east) float32 186.69469 ... 550.79767\n    UDRUNOFF     (member, time, south_north, west_east) float32 560.2294 ... 903.26166\n    ACCPRCP      (member, time, south_north, west_east) float32 1682.4382 ... 1631.8362\n    ACCECAN      (member, time, south_north, west_east) float32 131.5012 ... 127.482864\n    ACCEDIR      (member, time, south_north, west_east) float32 132.10272 ... 145.20123\n    ACCETRAN     (member, time, south_north, west_east) float32 467.5134 ... 551.33655\n    SMOISEQ      (member, time, south_north, soil_layers_stag, west_east) float32 9.96921e+36 ... 9.96921e+36\n    AREAXY       (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    SMCWTDXY     (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    DEEPRECHXY   (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    QSLATXY      (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    QRFSXY       (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    QSPRINGSXY   (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    RECHXY       (member, time, south_north, west_east) float32 0.0 0.0 ... 0.0\n    QRFXY        (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    QSPRINGXY    (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    FDEPTHXY     (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    RIVERCONDXY  (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    RIVERBEDXY   (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    EQZWT        (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36\n    PEXPXY       (member, time, south_north, west_east) float32 9.96921e+36 ... 9.96921e+36"
    }
}
