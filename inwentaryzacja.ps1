ForEach ($number in 30..50) { IF (Test-Connection -Count 1 -ComputerName "PLKRPC$number" -Quiet){ Get-WmiObject Win32_ComputerSystem -ComputerName "PLKRPC$number";
 (Get-WMIObject -ComputerName "PLKRPC$number" -class Win32_ComputerSystem | select username).username; wmic /NODE: "PLKRPC$number" bios get serialnumber
Function ConvertTo-Char
(	
	$Array
)
{
	$Output = ""
	ForEach($char in $Array)
	{	$Output += [char]$char -join ""
	}
	return $Output
}

$Query = Get-WmiObject -ComputerName "PLKRPC$number" -Query "Select * FROM WMIMonitorID" -Namespace root\wmi

$Results = ForEach ($Monitor in $Query)
{    
	New-Object PSObject -Property @{
		ComputerName = $env:ComputerName
		Active = $Monitor.Active
		Manufacturer = ConvertTo-Char($Monitor.ManufacturerName)
		UserFriendlyName = ConvertTo-Char($Monitor.userfriendlyname)
		SerialNumber = ConvertTo-Char($Monitor.serialnumberid)
		WeekOfManufacture = $Monitor.WeekOfManufacture
		YearOfManufacture = $Monitor.WeekOfManufacture
	}
}

$Results | Select ComputerName,Active,Manufacturer,UserFriendlyName,SerialNumber,WeekOfManufacture,YearOfManufacture﻿



}}