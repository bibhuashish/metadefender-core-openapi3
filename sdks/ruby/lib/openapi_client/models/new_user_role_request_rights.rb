=begin
#MetaDefender Core

### Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 

The version of the OpenAPI document: v4.18.0
Contact: feedback@opswat.com
Generated by: https://openapi-generator.tech
OpenAPI Generator version: 4.3.0

=end

require 'date'

module OpenapiClient
  # A list of rights for each permission
  class NewUserRoleRequestRights
    # What permissions are allowed for Node.
    attr_accessor :agents

    # What permissions are allowed for Certificates.
    attr_accessor :cert

    # What permissions are allowed for Configuration logs.
    attr_accessor :configlog

    # What permissions are allowed for Engines and Modules.
    attr_accessor :engines

    # What permissions are allowed for External actions (External Scanner/Post Actions).
    attr_accessor :external

    # What permissions are allowed for managing the License.
    attr_accessor :license

    # What permissions are allowed for managing the Quarantine.
    attr_accessor :quarantine

    # What permissions are allowed for managing the retention policies.
    attr_accessor :retention

    # What permissions are allowed for managing the workflow rules.
    attr_accessor :rule

    # What permissions are allowed for managing analysis actions.
    attr_accessor :scan

    # What permissions are allowed for managing the analysis logs.
    attr_accessor :scanlog

    # What permissions are allowed for managing the Whitelist/blacklist defined in the Inventory.
    attr_accessor :skip

    # What permissions are allowed for managing the update configuration.
    attr_accessor :update

    # What permissions are allowed for managing the update logs.
    attr_accessor :updatelog

    # What permissions are allowed for managing the users.
    attr_accessor :users

    # What permissions are allowed for managing the workflow templates.
    attr_accessor :workflow

    # What permissions are allowed for managing the network zones.
    attr_accessor :zone

    # Attribute mapping from ruby-style variable name to JSON key.
    def self.attribute_map
      {
        :'agents' => :'agents',
        :'cert' => :'cert',
        :'configlog' => :'configlog',
        :'engines' => :'engines',
        :'external' => :'external',
        :'license' => :'license',
        :'quarantine' => :'quarantine',
        :'retention' => :'retention',
        :'rule' => :'rule',
        :'scan' => :'scan',
        :'scanlog' => :'scanlog',
        :'skip' => :'skip',
        :'update' => :'update',
        :'updatelog' => :'updatelog',
        :'users' => :'users',
        :'workflow' => :'workflow',
        :'zone' => :'zone'
      }
    end

    # Attribute type mapping.
    def self.openapi_types
      {
        :'agents' => :'RolePermissionObject',
        :'cert' => :'RolePermissionObject',
        :'configlog' => :'RolePermissionObject',
        :'engines' => :'RolePermissionObject',
        :'external' => :'RolePermissionObject',
        :'license' => :'RolePermissionObject',
        :'quarantine' => :'RolePermissionObject',
        :'retention' => :'RolePermissionObject',
        :'rule' => :'RolePermissionObject',
        :'scan' => :'RolePermissionObject',
        :'scanlog' => :'RolePermissionObject',
        :'skip' => :'RolePermissionObject',
        :'update' => :'RolePermissionObject',
        :'updatelog' => :'RolePermissionObject',
        :'users' => :'RolePermissionObject',
        :'workflow' => :'RolePermissionObject',
        :'zone' => :'RolePermissionObject'
      }
    end

    # List of attributes with nullable: true
    def self.openapi_nullable
      Set.new([
      ])
    end

    # Initializes the object
    # @param [Hash] attributes Model attributes in the form of hash
    def initialize(attributes = {})
      if (!attributes.is_a?(Hash))
        fail ArgumentError, "The input argument (attributes) must be a hash in `OpenapiClient::NewUserRoleRequestRights` initialize method"
      end

      # check to see if the attribute exists and convert string to symbol for hash key
      attributes = attributes.each_with_object({}) { |(k, v), h|
        if (!self.class.attribute_map.key?(k.to_sym))
          fail ArgumentError, "`#{k}` is not a valid attribute in `OpenapiClient::NewUserRoleRequestRights`. Please check the name to make sure it's valid. List of attributes: " + self.class.attribute_map.keys.inspect
        end
        h[k.to_sym] = v
      }

      if attributes.key?(:'agents')
        self.agents = attributes[:'agents']
      end

      if attributes.key?(:'cert')
        self.cert = attributes[:'cert']
      end

      if attributes.key?(:'configlog')
        self.configlog = attributes[:'configlog']
      end

      if attributes.key?(:'engines')
        self.engines = attributes[:'engines']
      end

      if attributes.key?(:'external')
        self.external = attributes[:'external']
      end

      if attributes.key?(:'license')
        self.license = attributes[:'license']
      end

      if attributes.key?(:'quarantine')
        self.quarantine = attributes[:'quarantine']
      end

      if attributes.key?(:'retention')
        self.retention = attributes[:'retention']
      end

      if attributes.key?(:'rule')
        self.rule = attributes[:'rule']
      end

      if attributes.key?(:'scan')
        self.scan = attributes[:'scan']
      end

      if attributes.key?(:'scanlog')
        self.scanlog = attributes[:'scanlog']
      end

      if attributes.key?(:'skip')
        self.skip = attributes[:'skip']
      end

      if attributes.key?(:'update')
        self.update = attributes[:'update']
      end

      if attributes.key?(:'updatelog')
        self.updatelog = attributes[:'updatelog']
      end

      if attributes.key?(:'users')
        self.users = attributes[:'users']
      end

      if attributes.key?(:'workflow')
        self.workflow = attributes[:'workflow']
      end

      if attributes.key?(:'zone')
        self.zone = attributes[:'zone']
      end
    end

    # Show invalid properties with the reasons. Usually used together with valid?
    # @return Array for valid properties with the reasons
    def list_invalid_properties
      invalid_properties = Array.new
      invalid_properties
    end

    # Check to see if the all the properties in the model are valid
    # @return true if the model is valid
    def valid?
      true
    end

    # Checks equality by comparing each attribute.
    # @param [Object] Object to be compared
    def ==(o)
      return true if self.equal?(o)
      self.class == o.class &&
          agents == o.agents &&
          cert == o.cert &&
          configlog == o.configlog &&
          engines == o.engines &&
          external == o.external &&
          license == o.license &&
          quarantine == o.quarantine &&
          retention == o.retention &&
          rule == o.rule &&
          scan == o.scan &&
          scanlog == o.scanlog &&
          skip == o.skip &&
          update == o.update &&
          updatelog == o.updatelog &&
          users == o.users &&
          workflow == o.workflow &&
          zone == o.zone
    end

    # @see the `==` method
    # @param [Object] Object to be compared
    def eql?(o)
      self == o
    end

    # Calculates hash code according to all attributes.
    # @return [Integer] Hash code
    def hash
      [agents, cert, configlog, engines, external, license, quarantine, retention, rule, scan, scanlog, skip, update, updatelog, users, workflow, zone].hash
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def self.build_from_hash(attributes)
      new.build_from_hash(attributes)
    end

    # Builds the object from hash
    # @param [Hash] attributes Model attributes in the form of hash
    # @return [Object] Returns the model itself
    def build_from_hash(attributes)
      return nil unless attributes.is_a?(Hash)
      self.class.openapi_types.each_pair do |key, type|
        if type =~ /\AArray<(.*)>/i
          # check to ensure the input is an array given that the attribute
          # is documented as an array but the input is not
          if attributes[self.class.attribute_map[key]].is_a?(Array)
            self.send("#{key}=", attributes[self.class.attribute_map[key]].map { |v| _deserialize($1, v) })
          end
        elsif !attributes[self.class.attribute_map[key]].nil?
          self.send("#{key}=", _deserialize(type, attributes[self.class.attribute_map[key]]))
        end # or else data not found in attributes(hash), not an issue as the data can be optional
      end

      self
    end

    # Deserializes the data based on type
    # @param string type Data type
    # @param string value Value to be deserialized
    # @return [Object] Deserialized data
    def _deserialize(type, value)
      case type.to_sym
      when :DateTime
        DateTime.parse(value)
      when :Date
        Date.parse(value)
      when :String
        value.to_s
      when :Integer
        value.to_i
      when :Float
        value.to_f
      when :Boolean
        if value.to_s =~ /\A(true|t|yes|y|1)\z/i
          true
        else
          false
        end
      when :Object
        # generic object (usually a Hash), return directly
        value
      when /\AArray<(?<inner_type>.+)>\z/
        inner_type = Regexp.last_match[:inner_type]
        value.map { |v| _deserialize(inner_type, v) }
      when /\AHash<(?<k_type>.+?), (?<v_type>.+)>\z/
        k_type = Regexp.last_match[:k_type]
        v_type = Regexp.last_match[:v_type]
        {}.tap do |hash|
          value.each do |k, v|
            hash[_deserialize(k_type, k)] = _deserialize(v_type, v)
          end
        end
      else # model
        OpenapiClient.const_get(type).build_from_hash(value)
      end
    end

    # Returns the string representation of the object
    # @return [String] String presentation of the object
    def to_s
      to_hash.to_s
    end

    # to_body is an alias to to_hash (backward compatibility)
    # @return [Hash] Returns the object in the form of hash
    def to_body
      to_hash
    end

    # Returns the object in the form of hash
    # @return [Hash] Returns the object in the form of hash
    def to_hash
      hash = {}
      self.class.attribute_map.each_pair do |attr, param|
        value = self.send(attr)
        if value.nil?
          is_nullable = self.class.openapi_nullable.include?(attr)
          next if !is_nullable || (is_nullable && !instance_variable_defined?(:"@#{attr}"))
        end
        
        hash[param] = _to_hash(value)
      end
      hash
    end

    # Outputs non-array value in the form of hash
    # For object, use to_hash. Otherwise, just return the value
    # @param [Object] value Any valid value
    # @return [Hash] Returns the value in the form of hash
    def _to_hash(value)
      if value.is_a?(Array)
        value.compact.map { |v| _to_hash(v) }
      elsif value.is_a?(Hash)
        {}.tap do |hash|
          value.each { |k, v| hash[k] = _to_hash(v) }
        end
      elsif value.respond_to? :to_hash
        value.to_hash
      else
        value
      end
    end
  end
end