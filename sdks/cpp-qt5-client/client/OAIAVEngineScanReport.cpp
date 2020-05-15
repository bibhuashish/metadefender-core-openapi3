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

#include "OAIAVEngineScanReport.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIAVEngineScanReport::OAIAVEngineScanReport(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIAVEngineScanReport::OAIAVEngineScanReport() {
    this->initializeModel();
}

OAIAVEngineScanReport::~OAIAVEngineScanReport() {}

void OAIAVEngineScanReport::initializeModel() {

    m_def_time_isSet = false;
    m_def_time_isValid = false;

    m_eng_id_isSet = false;
    m_eng_id_isValid = false;

    m_location_isSet = false;
    m_location_isValid = false;

    m_scan_result_i_isSet = false;
    m_scan_result_i_isValid = false;

    m_scan_time_isSet = false;
    m_scan_time_isValid = false;

    m_threat_found_isSet = false;
    m_threat_found_isValid = false;

    m_wait_time_isSet = false;
    m_wait_time_isValid = false;
}

void OAIAVEngineScanReport::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIAVEngineScanReport::fromJsonObject(QJsonObject json) {

    m_def_time_isValid = ::OpenAPI::fromJsonValue(def_time, json[QString("def_time")]);
    m_def_time_isSet = !json[QString("def_time")].isNull() && m_def_time_isValid;

    m_eng_id_isValid = ::OpenAPI::fromJsonValue(eng_id, json[QString("eng_id")]);
    m_eng_id_isSet = !json[QString("eng_id")].isNull() && m_eng_id_isValid;

    m_location_isValid = ::OpenAPI::fromJsonValue(location, json[QString("location")]);
    m_location_isSet = !json[QString("location")].isNull() && m_location_isValid;

    m_scan_result_i_isValid = ::OpenAPI::fromJsonValue(scan_result_i, json[QString("scan_result_i")]);
    m_scan_result_i_isSet = !json[QString("scan_result_i")].isNull() && m_scan_result_i_isValid;

    m_scan_time_isValid = ::OpenAPI::fromJsonValue(scan_time, json[QString("scan_time")]);
    m_scan_time_isSet = !json[QString("scan_time")].isNull() && m_scan_time_isValid;

    m_threat_found_isValid = ::OpenAPI::fromJsonValue(threat_found, json[QString("threat_found")]);
    m_threat_found_isSet = !json[QString("threat_found")].isNull() && m_threat_found_isValid;

    m_wait_time_isValid = ::OpenAPI::fromJsonValue(wait_time, json[QString("wait_time")]);
    m_wait_time_isSet = !json[QString("wait_time")].isNull() && m_wait_time_isValid;
}

QString OAIAVEngineScanReport::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIAVEngineScanReport::asJsonObject() const {
    QJsonObject obj;
    if (m_def_time_isSet) {
        obj.insert(QString("def_time"), ::OpenAPI::toJsonValue(def_time));
    }
    if (m_eng_id_isSet) {
        obj.insert(QString("eng_id"), ::OpenAPI::toJsonValue(eng_id));
    }
    if (m_location_isSet) {
        obj.insert(QString("location"), ::OpenAPI::toJsonValue(location));
    }
    if (m_scan_result_i_isSet) {
        obj.insert(QString("scan_result_i"), ::OpenAPI::toJsonValue(scan_result_i));
    }
    if (m_scan_time_isSet) {
        obj.insert(QString("scan_time"), ::OpenAPI::toJsonValue(scan_time));
    }
    if (m_threat_found_isSet) {
        obj.insert(QString("threat_found"), ::OpenAPI::toJsonValue(threat_found));
    }
    if (m_wait_time_isSet) {
        obj.insert(QString("wait_time"), ::OpenAPI::toJsonValue(wait_time));
    }
    return obj;
}

QString OAIAVEngineScanReport::getDefTime() const {
    return def_time;
}
void OAIAVEngineScanReport::setDefTime(const QString &def_time) {
    this->def_time = def_time;
    this->m_def_time_isSet = true;
}

QString OAIAVEngineScanReport::getEngId() const {
    return eng_id;
}
void OAIAVEngineScanReport::setEngId(const QString &eng_id) {
    this->eng_id = eng_id;
    this->m_eng_id_isSet = true;
}

QString OAIAVEngineScanReport::getLocation() const {
    return location;
}
void OAIAVEngineScanReport::setLocation(const QString &location) {
    this->location = location;
    this->m_location_isSet = true;
}

qint32 OAIAVEngineScanReport::getScanResultI() const {
    return scan_result_i;
}
void OAIAVEngineScanReport::setScanResultI(const qint32 &scan_result_i) {
    this->scan_result_i = scan_result_i;
    this->m_scan_result_i_isSet = true;
}

qint32 OAIAVEngineScanReport::getScanTime() const {
    return scan_time;
}
void OAIAVEngineScanReport::setScanTime(const qint32 &scan_time) {
    this->scan_time = scan_time;
    this->m_scan_time_isSet = true;
}

QString OAIAVEngineScanReport::getThreatFound() const {
    return threat_found;
}
void OAIAVEngineScanReport::setThreatFound(const QString &threat_found) {
    this->threat_found = threat_found;
    this->m_threat_found_isSet = true;
}

qint32 OAIAVEngineScanReport::getWaitTime() const {
    return wait_time;
}
void OAIAVEngineScanReport::setWaitTime(const qint32 &wait_time) {
    this->wait_time = wait_time;
    this->m_wait_time_isSet = true;
}

bool OAIAVEngineScanReport::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_def_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_eng_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_location_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scan_result_i_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_scan_time_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_threat_found_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_wait_time_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIAVEngineScanReport::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI