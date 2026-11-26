# CRC Cards: UC-05 Create Purchase Request

Each card lists one class, its responsibilities, and the classes it collaborates with. Layer and stereotype are shown for reference.

---

### Card 1: PurchaseRequestWindow «view» (View Layer)

| Responsibilities | Collaborators |
|---|---|
| Display the shortage items and the request form | PurchaseRequestHandler |
| Collect quantities, justification, priority, required date, and estimated value from the manager | |
| Display the saved request reference and status Pending Approval | |
| Display the split-request warning when the handler flags related requests | |

---

### Card 2: PurchaseRequestHandler «controller» (Domain Layer)

| Responsibilities | Collaborators |
|---|---|
| Coordinate the Create Purchase Request use case | PurchaseRequestWindow |
| Retrieve shortage items from data access | PurchaseRequestDA |
| Create a PurchaseRequest from the entered details | PurchaseRequest |
| Check for related or split requests before saving | PurchaseRequestDA |
| Save the request with status Pending Approval | PurchaseRequestDA |
| Look up the required approver level for the request value | ProcurementPolicy |
| Create the RequestApproval record for the approver | RequestApproval |
| Return the confirmation to the window | PurchaseRequestWindow |

---

### Card 3: PurchaseRequest «entity» (Domain Layer)

| Responsibilities | Collaborators |
|---|---|
| Hold request data: reference, date, justification, priority, required date, estimated total | PurchaseRequestItem |
| Validate the request details | |
| Hold status (Pending Approval, Approved for Sourcing, etc.) | RequestApproval |
| Report whether the request is approved for sourcing | |
| Hold the list of requested items | |

---

### Card 4: PurchaseRequestItem «entity» (Domain Layer)

| Responsibilities | Collaborators |
|---|---|
| Hold the product, quantity, and description for one line of the request | PurchaseRequest, Product |
| Validate the quantity | |
| Update the quantity | |

---

### Card 5: ProcurementPolicy «entity» (Domain Layer)

| Responsibilities | Collaborators |
|---|---|
| Hold the approved, versioned authority matrix | RequestApproval |
| Return the authority level required for a given amount | PurchaseRequestHandler |
| Return the required number of quotations for a given amount | RFQ |

---

### Card 6: RequestApproval «entity» (Domain Layer)

| Responsibilities | Collaborators |
|---|---|
| Hold the approval decision, rationale, and timestamp | PurchaseRequest, User |
| Record the approver's decision | |
| Ensure the approver is not the requester | User |

---

### Card 7: PurchaseRequestDA «dataAccess» (Data Access Layer)

| Responsibilities | Collaborators |
|---|---|
| Query products below the required stock level | Inventory, Database |
| Query open requests related by product and date | Database |
| Insert the purchase request with its reference and creator | Database |
| Return the saved request ID and reference | PurchaseRequestHandler |

---

### Supporting collaborators outside this use case

| Class | Role in UC-05 |
|---|---|
| Inventory «entity» | Supplies available and reserved stock used to identify shortages (UC-04) |
| Product «entity» | Supplies product codes for each request item |
| User «entity» | Identifies the requester and the approver |
| Database | Stores requests and returns query results |
