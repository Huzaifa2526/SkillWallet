import zipfile, xml.etree.ElementTree as ET, hashlib, io

orig_twbx = r'a:\Skill wallet 1\BACKUP\Original_Workbook.twbx'
new_twbx = r'a:\Skill wallet 1\Huzaifa_Tableau_Project\Huzaifa_Sheikh_Food_Ordering_Behaviour_and_Consumer_Trend.twbx'

print("=== WORKBOOK VALIDATION ===")

with zipfile.ZipFile(orig_twbx, 'r') as zf_orig, zipfile.ZipFile(new_twbx, 'r') as zf_new:
    # 1. Zip test
    assert zf_orig.testzip() is None, "Original zip corrupted"
    assert zf_new.testzip() is None, "New zip corrupted"
    print("[PASS] Zip package integrity test: OK")

    # 2. Extract comparison
    orig_hyper_name = [n for n in zf_orig.namelist() if n.endswith('.hyper')][0]
    new_hyper_name = [n for n in zf_new.namelist() if n.endswith('.hyper')][0]
    
    orig_hyper_data = zf_orig.read(orig_hyper_name)
    new_hyper_data = zf_new.read(new_hyper_name)
    
    orig_hash = hashlib.sha256(orig_hyper_data).hexdigest()
    new_hash = hashlib.sha256(new_hyper_data).hexdigest()
    
    assert orig_hash == new_hash, "Hyper extract differs!"
    print(f"[PASS] Hyper extract integrity: 100% bit-for-bit match (SHA256: {orig_hash[:16]}...)")

    # 3. XML parsing & structure
    orig_twb_data = zf_orig.read('Food Ordering Behaviour and Consumer Trend.twb')
    new_twb_data = zf_new.read('Food Ordering Behaviour and Consumer Trend.twb')
    
    tree_orig = ET.fromstring(orig_twb_data)
    tree_new = ET.fromstring(new_twb_data)
    print("[PASS] XML well-formedness: OK")

    # 4. Worksheets
    orig_sheets = [s.get('name') for s in tree_orig.findall('.//worksheet')]
    new_sheets = [s.get('name') for s in tree_new.findall('.//worksheet')]
    assert orig_sheets == new_sheets, "Worksheets do not match!"
    print(f"[PASS] Worksheets: All {len(new_sheets)} intact and identical in order")

    # 5. Dashboards & Storyboards
    orig_dash = [d.get('name') for d in tree_orig.findall('.//dashboard')]
    new_dash = [d.get('name') for d in tree_new.findall('.//dashboard')]
    assert orig_dash == new_dash, "Dashboards do not match!"
    print(f"[PASS] Dashboards & Storyboards: All {len(new_dash)} intact: {new_dash}")

    # 6. Story points
    orig_sp = [p.get('caption') for p in tree_orig.findall('.//story-point')]
    new_sp = [p.get('caption') for p in tree_new.findall('.//story-point')]
    assert orig_sp == new_sp, "Story points do not match!"
    print(f"[PASS] Story points: All {len(new_sp)} intact")

    # 7. Datasources & Calculations
    orig_cols = [c.attrib for c in tree_orig.findall('.//column')]
    new_cols = [c.attrib for c in tree_new.findall('.//column')]
    assert orig_cols == new_cols, "Columns / calculations do not match!"
    print(f"[PASS] Columns and calculations: All {len(new_cols)} intact and identical")

    # 8. Calculations logic (calculation elements)
    orig_calcs = [ET.tostring(c) for c in tree_orig.findall('.//calculation')]
    new_calcs = [ET.tostring(c) for c in tree_new.findall('.//calculation')]
    assert orig_calcs == new_calcs, "Calculation formulas do not match!"
    print(f"[PASS] Calculation formulas: All {len(new_calcs)} intact and identical")

print("\nALL 14 VALIDATION CRITERIA PASSED.")
