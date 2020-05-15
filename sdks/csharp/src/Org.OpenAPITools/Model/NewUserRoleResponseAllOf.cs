/* 
 * MetaDefender Core
 *
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  - -- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   - -- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;
using System.ComponentModel.DataAnnotations;
using OpenAPIDateConverter = Org.OpenAPITools.Client.OpenAPIDateConverter;

namespace Org.OpenAPITools.Model
{
    /// <summary>
    /// NewUserRoleResponseAllOf
    /// </summary>
    [DataContract]
    public partial class NewUserRoleResponseAllOf :  IEquatable<NewUserRoleResponseAllOf>, IValidatableObject
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="NewUserRoleResponseAllOf" /> class.
        /// </summary>
        [JsonConstructorAttribute]
        protected NewUserRoleResponseAllOf() { }
        /// <summary>
        /// Initializes a new instance of the <see cref="NewUserRoleResponseAllOf" /> class.
        /// </summary>
        /// <param name="editable">If the role can be altered or not. (required).</param>
        /// <param name="id">Internal used identifier (required).</param>
        public NewUserRoleResponseAllOf(bool editable = default(bool), int id = default(int))
        {
            // to ensure "editable" is required (not null)
            if (editable == null)
            {
                throw new InvalidDataException("editable is a required property for NewUserRoleResponseAllOf and cannot be null");
            }
            else
            {
                this.Editable = editable;
            }
            
            // to ensure "id" is required (not null)
            if (id == null)
            {
                throw new InvalidDataException("id is a required property for NewUserRoleResponseAllOf and cannot be null");
            }
            else
            {
                this.Id = id;
            }
            
        }
        
        /// <summary>
        /// If the role can be altered or not.
        /// </summary>
        /// <value>If the role can be altered or not.</value>
        [DataMember(Name="editable", EmitDefaultValue=false)]
        public bool Editable { get; set; }

        /// <summary>
        /// Internal used identifier
        /// </summary>
        /// <value>Internal used identifier</value>
        [DataMember(Name="id", EmitDefaultValue=false)]
        public int Id { get; set; }

        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class NewUserRoleResponseAllOf {\n");
            sb.Append("  Editable: ").Append(Editable).Append("\n");
            sb.Append("  Id: ").Append(Id).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public virtual string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="input">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object input)
        {
            return this.Equals(input as NewUserRoleResponseAllOf);
        }

        /// <summary>
        /// Returns true if NewUserRoleResponseAllOf instances are equal
        /// </summary>
        /// <param name="input">Instance of NewUserRoleResponseAllOf to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(NewUserRoleResponseAllOf input)
        {
            if (input == null)
                return false;

            return 
                (
                    this.Editable == input.Editable ||
                    (this.Editable != null &&
                    this.Editable.Equals(input.Editable))
                ) && 
                (
                    this.Id == input.Id ||
                    (this.Id != null &&
                    this.Id.Equals(input.Id))
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            unchecked // Overflow is fine, just wrap
            {
                int hashCode = 41;
                if (this.Editable != null)
                    hashCode = hashCode * 59 + this.Editable.GetHashCode();
                if (this.Id != null)
                    hashCode = hashCode * 59 + this.Id.GetHashCode();
                return hashCode;
            }
        }

        /// <summary>
        /// To validate all properties of the instance
        /// </summary>
        /// <param name="validationContext">Validation context</param>
        /// <returns>Validation Result</returns>
        IEnumerable<System.ComponentModel.DataAnnotations.ValidationResult> IValidatableObject.Validate(ValidationContext validationContext)
        {
            yield break;
        }
    }

}