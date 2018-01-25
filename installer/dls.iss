; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{6B0E2867-5810-4491-A86D-55B5C208C0FE}
AppName=Discord_Letters by Helgi
AppVersion=0.2
;AppVerName=Discord_Letters by Helgi 0.2
AppPublisher=Fisedush
AppPublisherURL=https://fisedush.com
AppSupportURL=https://fisedush.com
AppUpdatesURL=https://fisedush.com
DefaultDirName={pf}\Discord_Letters
DisableProgramGroupPage=yes
OutputDir=D:\Projects\discord_letters\2distribute
OutputBaseFilename=discord_letters setup
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "D:\Projects\discord_letters\2distribute\main.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\discord_letters\2distribute\dl_logo.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\discord_letters\2distribute\mainwindow.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\discord_letters\2distribute\updater.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\discord_letters\2distribute\updatewindow.ui"; DestDir: "{app}"; Flags: ignoreversion
Source: "D:\Projects\discord_letters\2distribute\version"; DestDir: "{app}"; Flags: ignoreversion
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\Discord_Letters by Helgi"; Filename: "{app}\main.exe"
Name: "{commondesktop}\Discord_Letters by Helgi"; Filename: "{app}\main.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\main.exe"; Description: "{cm:LaunchProgram,Discord_Letters by Helgi}"; Flags: nowait postinstall skipifsilent

