# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:29:29 2018

@author: Subha Karanam
"""

class Cleaning:
    
    #drop irrelevant columns
    def IrrCols(myDataframe):
        drop_col = ['Contracting Agency ID', 'Contracting Office ID','Contracting Office Region',
                    'PIID', 'Modification Number','Transaction Number', 'Referenced  IDV PIID','Effective Date',
                    'Completion Date', 'Last Date to Order','Funding Department ID','Funding Agency ID',
                    'Funding Office ID','Foreign Funding','Product or Service Code',
                    'Inherently Governmental Function','NAICS Code','Principal Place of Performance Location Code',
                    'Principal Place of Performance State Code','Principal Place of Performance Congressional District',
                    'Principal Place of Performance Zip Code','Principal Place of Performance Country Name',
                    'Country of Product or Service Origin','Place of Manufacture','Extent Competed',
                    'Other Than Full and Open Competition','Other Than Full and Open Competition',
                    'Solicitation Procedures','Type of Set Aside','Local Area Set Aside','Evaluated Preference',
                    'SBIR/STTR','Fair Opportunity/Limited Sources','Commercial Item Acquisition Procedures',
                    'Award Type','Reason For Modification','DUNS Number','Global DUNS Number','Vendor Address Zip Code',
                    'Vendor Address Country Name','SAM Exception Type','Vendor Congressional District',
                    'Is Vendor Business Type - Contracts','Is Vendor Business Type - Grants',
                    'Is Vendor Business Type - Both (Contracts and Grants)','Is Vendor Business Type - U.S. Federal Government',
                    'Is Vendor Business Type - Federally Funded Research and Development Corporation',
                    'Is Vendor Business Type - Federal Agency','Is Vendor Business Type - U.S. State Government',
                    'Is Vendor Business Type - U.S. Local Government','Is Vendor Business Type - City',
                    'Is Vendor Business Type - County','Is Vendor Business Type - Inter Municipal',
                    'Is Vendor Business Type - Local Government Owned','Is Vendor Business Type - Municipality',
                    'Is Vendor Business Type - School District','Is Vendor Business Type - Township',
                    'Is Vendor Business Type - U.S. Tribal Government','Is Vendor Business Type - Foreign Government',
                    'Is Vendor Business Type - Airport Authority','Is Vendor Business Type - Council Of Governments',
                    'Is Vendor Business Type - Housing Authorities Public or Tribal','Is Vendor Business Type - Interstate Entity',
                    'Is Vendor Business Type - Planning Commission','Is Vendor Business Type - Port Authority',
                    'Is Vendor Business Type - Transit Authority','Is Vendor Business Type - Corporate Entity, Not Tax Exempt',
                    'Is Vendor Business Type - Corporate Entity, Tax Exempt','Is Vendor Business Type - Subchapter S Corporation',
                    'Is Vendor Business Type - Limited Liability Corporation','Is Vendor Business Type - Partnership or Limited Liability Partnership',
                    'Is Vendor Business Type - Sole Proprietorship','Is Vendor Business Type - Small Agricultural Cooperative',
                    'Is Vendor Business Type - International Organization','Is Vendor Business Type - U.S. Government Entity',
                    'Is Vendor Business Type - Foreign Owned','Is Vendor Business Type - For Profit Organization',
                    'Is Vendor Business Type - Non Profit Organization','Is Vendor Business Type - Other Not For Profit Organization',
                    'Is Vendor Business Type - Other Not For Profit Organization','Is Vendor Business Type - Community Developed Corporation Owned Firm',
                    'Is Vendor Business Type - Labor Surplus Area Firm','Is Vendor Business Type - Self-Certifed Small Disadvantaged Business',
                    'Is Vendor Business Type - Veteran Owned Business','Is Vendor Business Type - Service Disabled Veteran Owned Business',
                    'Is Vendor Business Type - Woman Owned Business','Is Vendor Business Type - Women Owned Small Business',
                    'Is Vendor Business Type - Economically Disadvantaged Women Owned Small Business',
                    'Is Vendor Business Type - Joint Venture Women Owned Small Business',
                    'Is Vendor Business Type - Joint Venture Economically Disadvantaged Women Owned Small Business',
                    'Is Vendor Business Type - Minority Owned Business','Is Vendor Business Type - Subcontinent Asian (Asian-Indian) American Owned',
                    'Is Vendor Business Type - Asian-Pacific American Owned','Is Vendor Business Type - Black American Owned',
                    'Is Vendor Business Type - Hispanic American Owned','Is Vendor Business Type - Native American Owned',
                    'Is Vendor Business Type - Other Minority Owned','Is Vendor Business Type - Community Development Corporation',
                    'Is Vendor Business Type - Domestic Shelter','Is Vendor Business Type - Foundation','Is Vendor Business Type - Hospital',
                    'Is Vendor Business Type - Veterinary Hospital','Is Vendor Business Type - Educational Institution',
                    'Is Vendor Business Type - 1862 Land Grant College','Is Vendor Business Type - 1890 Land Grant College',
                    'Is Vendor Business Type - 1994 Land Grant College','Is Vendor Business Type - HBCU Concern',
                    'Is Vendor Business Type - Hispanic Servicing Institution','Is Vendor Business Type - Minority Institutions',
                    'Is Vendor Business Type - Private University Or College','Is Vendor Business Type - School Of Forestry',
                    'Is Vendor Business Type - State Controlled Institution of Higher Learning','Is Vendor Business Type - Tribal College',
                    'Is Vendor Business Type - Veterinary College','Is Vendor Business Type - Alaskan Native Servicing Institution',
                    'Is Vendor Business Type - Native Hawaiian Servicing Institution','Is Vendor Business Type - Alaskan Native Corporation Owned Firm',
                    'Is Vendor Business Type - Manufacturer Of Goods',
                    'Is Vendor Business Type - DoT Certified Disadvantaged Business Enterprise','Is Vendor Business Type - American Indian',
                    'Is Vendor Business Type - Indian Tribe','Is Vendor Business Type - Native Hawaiian Organization Owned Firm',
                    'Is Vendor Business Type - Tribally Owned','Is Vendor Business Type - Small Disadvantaged Business',
                    'Is Vendor Business Type - 8A Program Participant','Is Vendor Business Type - HUBZone Firm','Is Vendor Business Type - 8A Joint Venture',
                    'Is Vendor Business Type - (JWOD) Sheltered Workshop','Is Vendor Business Type - Emerging Small Business',
                    'Country Of Incorporation','State Of Incorporation','Contracting Officer Business Size Determination','Clinger Cohen Act',
                    'Service Contract Act','Walsh Healey Act','Davis Bacon Act','Other Statutory Authority','Interagency Contracting Authority',
                    'Treasury Account Symbol Initiative','Treasury Account Symbol Agency Identifier','Treasury Account Symbol Main Account',
                    'Treasury Account Symbol Sub Account','Number of Actions','Base and Exercised Options Value','Base and All Options Value']
        print("Number of unneccessary columns dropped:")
        print(len(drop_col))
        myDataframe = myDataframe.drop(columns = drop_col)
        return myDataframe
    
    #removing columns which contain private, uneccessary information
    def privateColumns(myDataframe):
        drop_col = ['Contracting Office Name','Funding Department Name','Domestic or Foreign Entity',
                    'Is Performance Based Service Acquisition','Type of Contract',
                    'Description of Requirement','NAICS Description',
                    'Principal Place of Performance County Name',
                    'Principal Place of Performance Location Name','Vendor Name','Global Vendor Name',
                    'Vendor Address Line 1','Vendor Address Line 2','Vendor Address City',
                    ]
        print("Number of columns dropped to preserve privacy:")
        print(len(drop_col))
        myDataframe = myDataframe.drop(columns = drop_col)
        return myDataframe 
    
    #removing data instances which have zero action obligation
    def zeroDollars(myDataframe):
        valuelist = ["0.00"]
        before = len(myDataframe.index)
        myDataframe = myDataframe[~myDataframe["Action Obligation"].isin(valuelist)]
        after = len(myDataframe.index)
        print("\n the number of values dropped = ", before - after, "\n")
        return myDataframe[:-1]
        
        
    
        