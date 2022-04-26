import cx_Freeze

cx_Freeze.setup(
    name    = "Rendering Engine",
    version = '0.22.24.26',
    description = 'PyGame 2 Engine',
    author = 'gabrielmtzcarrillo',

    options = { 
        "build_exe" : {
                "packages" : ["pygame"] , 
                "include_files" : ["assets/"]
            }
    },
    
    executables = [ 
        cx_Freeze.Executable(
            "main.py", 
            base = "Win32GUI"
        ) 
    ]
)
