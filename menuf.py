import marshal, os
try:
	import lib, base64
except:
	os.system('pip install lib');os.system('pip install base64')
xvideo = (base64.b64decode('''IyMjIyMjIyMjIyMjIyMjIyMjIyMjCiMgRlVOw4fDlUVTICYgTU9EVUxPUyAjCiMjIyMjIyMjIyMjIyMjIyMjIyMjIwoKCmdsb2JhbCBSLEIsQyxZLEcsUlQsQ1ksQ08KQ089J1wwMzNbbSc7Uj0nXDAzM1sxOzMxbSc7Qj0nXDAzM1sxOzM0bSc7Qz0nXDAzM1sxOzM3bSc7Q1k9J1wwMzNbMTszNm0nO1k9J1wwMzNbMTszM20nO0c9J1wwMzNbMTszMm0nO1JUPSdcMDMzWzswbSc7Tk9fRk9STUFUPSJcMDMzWzBtIjtDX0dSRVk4OT0iXDAzM1szODs1OzI1NG0iO0NfUkVEMT0iXDAzM1s0ODs1OzE5Nm0iCmltcG9ydCBvcywgc3lzLCBweWZpZ2xldApmcm9tIHRpbWUgaW1wb3J0IHNsZWVwCgpkZWYgY2xlYXIoKToKCW9zLnN5c3RlbSgnY2xlYXInKQoKCiMjIyMjIyMjIyMjIyMjIyMjIwojIE1FTlUgUFJJTkNJUEFMICMKIyMjIyMjIyMjIyMjIyMjIyMjCgpwcmludChmJ3tHfSAgICAgIC0tLSBGRUlUTyBQT1Ige0J9IHtHfSBMSVBFWklOe0J9IDwvPiB7R30tLS0nKQpyZXN1bHQgPSBweWZpZ2xldC5maWdsZXRfZm9ybWF0KCJMaXBlTWVudSIsIGZvbnQgPSAiY29zbWljIiApCnByaW50KGYnJyd7Q317R30Ke3Jlc3VsdH0nJycpCnByaW50KGYnICAgIHtDfT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09JykKCnByaW50KGYnICAgIHtDfT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09JykKcHJpbnQoZid7Q30gICAgW3tHfSAxe0N9IF17Un0gQkFJWEFSIE1FVEFTUExPSVQoRE8gIEd1c2htYXp1a28pIHtHfScpCnByaW50KGYne0N9ICAgIFt7R30gMntDfSBde1J9IE5NQVAnKQpwcmludChmJ3tDfSAgICBbe0d9IDN7Q30gXXtSfVRIRUhBUlZFU1RFUicpCnByaW50KGYne0N9ICAgIFt7R30gNHtDfSBde1J9IGNyaWFkb3InKQpwcmludChmJ3tDfSAgICBbe0d9IDV7Q30gXXtSfSBNRVUgQ0hBVCcpCnByaW50KGYne0N9ICAgIFt7R30gNntDfSBde1J9IFJPT1QgTk8gVEVSTVVYJykKcHJpbnQoZicgICAge0N9PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT09PT0nKQpwcmludChmJ3tDfSAgIFt7Un0gKiB7Q31dIERJR0lURSBBIE9QQ0FPIFBPUiBOVU1FUk8nKQpvcGMgPSBpbnB1dChmJ3tHfVxuXG4gICAtLT4gU0VMRUNJT05FIEEgT1DDh8ODTyBERVNFSkFEQTogJykKCgoKaWYgb3BjID09ICcxJzoKCW9zLnN5c3RlbSgnJycKCXBrZyBpbnN0YWxsIHBvc3RncmVzcWwKCnBrZyBpbnN0YWxsIG9wZW5zc2ggd2dldCBjdXJsIGdpdCAteQoKd2dldCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vZ3VzaG1henVrby9tZXRhc3Bsb2l0X2luX3Rlcm11eC9tYXN0ZXIvbWV0YXNwbG9pdC5zaAoKY2htb2QgK3ggbWV0YXNwbG9pdC5zaAoKLi9tZXRhc3Bsb2l0LnNoJycnKQoKCmlmIG9wYyA9PSAnNCc6Cglvcy5zeXN0ZW0oJ3Rlcm11eC1vcGVuLXVybCBodHRwczovL1dBLm1lLys1NTM1ODgzMTc2ODEnKQoJCglyZXN1bHQgPSBweWZpZ2xldC5maWdsZXRfZm9ybWF0KCIgTWVudSIsIGZvbnQgPSAiY29zbWljIiApCgoKCmlmIG9wYyA9PSAnMyc6Cglvcy5zeXN0ZW0oJ2dpdCBjbG9uZSBodHRwczovL2dpdGh1Yi5jb20vbGFyYW1pZXMvdGhlSGFydmVzdGVyJykKCQoJCglpZiBvcGMgPT0gJzInOgoJCW9zLnN5c3RlbSgnZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9ubWFwL25tYXAnKQoJCQpyZXN1bHQgPSBweWZpZ2xldC5maWdsZXRfZm9ybWF0KCIgQlkgTElQRSIsIGZvbnQgPSAiY29zbWljIiApCnByaW50KGYnJyd7Q317R30Ke3Jlc3VsdH0nJycpCgppZiBvcGMgPT0gJzUnOgoJCW9zLnN5c3RlbSgndGVybXV4LW9wZW4tdXJsIGh0dHBzOi8vY2hhdC53aGF0c2FwcC5jb20vRkNKTTdib3pQT01BSnd3V3plQVU1aycpCgkJCgkJCmlmIG9wYyA9PSAnNic6Cglvcy5zeXN0ZW0oJycnCglhcHQgdXBkYXRlICYmIGFwdCAteSB1cGdyYWRlCgpwa2cgaW5zdGFsbCAteSBnaXQKCnBrZyBpbnN0YWxsIC15IHByb290Cgp0ZXJtdXgtc2V0dXAtc3RvcmFnZQoKZ2l0IGNsb25lIGh0dHBzOi8vZ2l0aHViLmNvbS9Bbm9ueW1vdXMtWnB0L1Qtcm9vdAoKY2QgVC1yb290CgpiYXNoIGluc3RhbGwuc2gKCi4vc3RhcnQgJycnKQ=='''))
exec(xvideo)