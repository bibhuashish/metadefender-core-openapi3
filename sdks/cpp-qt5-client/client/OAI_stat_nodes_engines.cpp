/**
 * MetaDefender Core
 * ## Developer Guide This is the API documentation for *MetaDefender Core Public API*.  If you would like to evaluate or have any questions about this documentation, please contact us via our [Contact Us](https://opswat.com/contact) form.  ## How to Interact with MetaDefender Core using REST Beginning with MetaDefender Core 4.x, OPSWAT recommends using the JSON-based REST API. The available methods are documented below. > _**Note**:_ MetaDefender API doesn't support chunk upload, however is recommended to stream the files to MetaDefender as part of the upload process.  --- ## File Analysis Process    MetaDefender's main functionality is to analyze large volumes with a high throughput. Depending on the configuration and licensed technologies, the analysis times can vary.    Below is a brief description of the API integration flow:    1. Upload a file for analysis (`POST /file`), which returns the `data_id`: [File Analysis](#operation/fileAnalysisPost)).           > _**Note**:_ The performance depends on:           > - number of nodes (scaling)     > - number of engines per node     > - type of file to be scanned     > - Metadefender Core and nodes' hardware       2. You have 2 ways to retrieve the analysis report:      - **Polling**: Fetch the result with previously received data_id (`GET /file/{data_id}` resource) until scan result belonging to data_id doesn't reach the 100 percent progress_percentage: ( [Fetch processing result](#operation/userLogin))        > _**Note**:_ Too many data_id requests can reduce performance. It is enough to just check every few hundred milliseconds.          - **Callbackurl**: Specify a callbackurl that will be called once the analysis is complete.     3. Retrieve the analysis results anytime after the analysis is completed with hash for files (md5, sha1, sha256) by calling [Fetch processing result](#operation/userLogin).      - The hash can be found in the scan results    4. Retrieve processed file (sanitized, redacted, watermarked, etc.) after the analysis is complete.      > _**Note**:_ Based on the configured retention policy, the files might be available for retrieval at a later time.   --- OPSWAT provides some sample codes on [GitHub](https://github.com/OPSWAT) to make it easier to understand how the MetaDefender REST API works. 
 *
 * The version of the OpenAPI document: v4.18.0
 * Contact: feedback@opswat.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAI_stat_nodes_engines.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAI_stat_nodes_engines::OAI_stat_nodes_engines(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAI_stat_nodes_engines::OAI_stat_nodes_engines() {
    this->initializeModel();
}

OAI_stat_nodes_engines::~OAI_stat_nodes_engines() {}

void OAI_stat_nodes_engines::initializeModel() {

    m_active_isSet = false;
    m_active_isValid = false;

    m_db_ver_isSet = false;
    m_db_ver_isValid = false;

    m_def_time_isSet = false;
    m_def_time_isValid = false;

    m_eng_name_isSet = false;
    m_eng_name_isValid = false;

    m_eng_ver_isSet = false;
    m_eng_ver_isValid = false;

    m_engine_type_isSet = false;
    m_engine_type_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;
}

void OAI_stat_nodes_engines::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAI_stat_nodes_engines::fromJsonObject(QJsonObject json) {

    m_active_isValid = ::OpenAPI::fromJsonValue(active, json[QString("active")]);
    m_active_isSet = !json[QString("active")].isNull() && m_active_isValid;

    m_db_ver_isValid = ::OpenAPI::fromJsonValue(db_ver, json[QString("db_ver")]);
    m_db_ver_isSet = !json[QString("db_ver")].isNull() && m_db_ver_isValid;

    m_def_time_isValid = ::OpenAPI::fromJsonValue(def_time, json[QString("def_time")]);
    m_def_time_isSet = !json[QString("def_time")].isNull() && m_def_time_isValid;

    m_eng_name_isValid = ::OpenAPI::fromJsonValue(eng_name, json[QString("eng_name")]);
    m_eng_name_isSet = !json[QString("eng_name")].isNull() && m_eng_name_isValid;

    m_eng_ver_isValid = ::OpenAPI::fromJsonValue(eng_ver, json[QString("eng_ver")]);
    m_eng_ver_isSet = !json[QString("eng_ver")].isNull() && m_eng_ver_isValid;

    m_engine_type_isValid = ::OpenAPI::fromJsonValue(engine_type, json[QString("engine_type")]);
    m_engine_type_isSet = !json[QString("engine_type")].isNull() && m_engine_type_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;
}

QString OAI_stat_nodes_engines::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAI_stat_nodes_engines::asJsonObject() const {
    QJsonObject obj;
    if (m_active_isSet) {
        obj.insert(QString("active"), ::OpenAPI::toJsonValue(active));
    }
    if (m_db_ver_isSet) {
        obj.insert(QString("db_ver"), ::OpenAPI::toJsonValue(db_ver));
    }
    if (m_def_time_isSet) {
        obj.insert(QString("def_time"), ::OpenAPI::toJsonValue(def_time));
    }
    if (m_eng_name_isSet) {
        obj.insert(QString("eng_name"), ::OpenAPI::toJsonValue(eng_name));
    }
    if (m_eng_ver_isSet) {
        obj.insert(QString("eng_ver"), ::OpenAPI::toJsonValue(eng_ver));
    }
    if (m_engine_type_isSet) {
        obj.insert(QString("engine_type"), ::OpenAPI::toJsonValue(engine_type));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(id));
    }
    return obj;
}

bool OAI_stat_nodes_engines::isActive() const {
    return active;
}
void OAI_stat_nodes_engines::setActive(const bool &active) {
    this->active = active;
    this->m_active_isSet = true;
}

QString OAI_stat_nodes_engines::getDbVer() const {
    return db_ver;
}
void OAI_stat_nodes_engines::setDbVer(const QString &db_ver) {
    this->db_ver = db_ver;
    this->m_db_ver_isSet = true;
}

QString OAI_stat_nodes_engines::getDefTime() const {
    return def_time;
}
void OAI_stat_nodes_engines::setDefTime(const QString &def_time) {
    this->def_time = def_time;
    this->m_def_time_isSet = true;
}

QString OAI_stat_nodes_engines::getEngName() const {
    return eng_name;
}
void OAI_stat_nodes_engines::setEngName(const QString &eng_name) {
    this->eng_name = eng_name;
    this->m_eng_name_isSet = true;
}

QString OAI_stat_nodes_engines::getEngVer() const {
    return eng_ver;
}
void OAI_stat_nodes_engines::setEngVer(const QString &eng_ver) {
    this->eng_ver = eng_ver;
    this->m_eng_ver_isSet = true;
}

QString OAI_stat_nodes_engines::getEngineType() const {
    return engine_type;
}
void OAI_stat_nodes_engines::setEngineType(const QString &engine_type) {
    this->engine_type = engine_type;
    this->m_engine_type_isSet = true;
}

QString OAI_stat_nodes_engines::getId() const {
    return id;
}
void OAI_stat_nodes_engines::setId(const QString &id) {
    this->id = id;
    this->m_id_isSet = true;
}

bool OAI_stat_nodes_engines::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_active_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_db_ver_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_def_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_eng_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_eng_ver_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_engine_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAI_stat_nodes_engines::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI