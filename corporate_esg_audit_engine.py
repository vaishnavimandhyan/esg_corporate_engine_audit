def run_corporate_esg_audit_engine():
 
 print("MFIN AUDITING LAB: SYSTEMATIC SUSTAINABILITY DATA RECONCILIATION")
 print("Audit Framework: Assurance Verification & Materiality Exception Testing")
 

# 1. Audit Parameters & Thresholds
 materiality_threshold = 0.05

# Audit Scope Data: Store Locations under review
 locations = ["London Flagship Hub", "Midlands Logistics Depot", "North-East Retail Center"]
 reported_carbon_emissions = [1250.00, 3400.00, 890.00]
 verified_operational_evidence = [1262.00, 3650.00, 840.00]

 print(f"Auditing Scope: Verifying internal controls for {len(locations)} primary operating centers.")
 print(f"Assurance Parameters: Materiality Limit established at {materiality_threshold * 100:.1f}% variance.")
 print("-" * 84)

# 2. Execute Data Reconciliation Loop
 total_reported = 0.0
 total_verified = 0.0
 exceptions_identified = 0

 for i in range(len(locations)):
  location_name = locations[i]
  reported_value = reported_carbon_emissions[i]
  verified_value = verified_operational_evidence[i]

  total_reported += reported_value
  total_verified += verified_value

# Audit Mathematics: Compute absolute variance percentage
  absolute_variance = abs(reported_value - verified_value)
  variance_percentage = absolute_variance / verified_value

  print(f"Location Ledger: {location_name}")
  print(f" Management Statement: {reported_value:,.2f} MT | Raw Evidence Log: {verified_value:,.2f} MT")
  print(f" Calculated Variance: {variance_percentage * 100:.2f}%")

# Materiality Testing: Check if the data discrepancy breaches the threshold
  if variance_percentage > materiality_threshold:
   audit_ruling = "DEFICIENCY IDENTIFIED: BREACHES MATERIALITY LIMIT"
   exceptions_identified += 1
  else:
   audit_ruling = "VERIFIED: ASSURANCE RECONCILIATION SUCCESSFUL"

  print(f" Audit Ruling: [{audit_ruling}]")
  print("-" * 84)

# 3. Aggregate Audit Summary Report
 aggregate_variance_percentage = abs(total_reported - total_verified) / total_verified

 if aggregate_variance_percentage > materiality_threshold or exceptions_identified > 0:
  final_opinion = "ADVERSE OPINION / UNRESOLVED DISCREPANCIES EXIST"
 else:
  final_opinion = "UNQUALIFIED OPINION / COMPLETE DATA RECONCILIATION"

 print("INDEPENDENT AUDIT ASSURANCE MEMO")
 print(f" Global Audit Opinion: [{final_opinion}]")
 print(f" Total Corporate Deficiencies: {exceptions_identified} Exception Logs Generated")
 print(f" Total Reported Footprint: {total_reported:,.2f} Metric Tons CO2")
 print(f" Total Reconciled Footprint: {total_verified:,.2f} Metric Tons CO2")
 print(f" Consolidated Variance: {aggregate_variance_percentage * 100:.2f}%")
 print("Quantitative Auditing Insight: Discrepancies between management disclosures and")
 print("independent operational logs require substantive internal control adjustments")
 print("to mitigate systemic greenwashing reporting risks and regulatory audit exposure.")
 

run_corporate_esg_audit_engine()
