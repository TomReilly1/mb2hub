import { onMounted, onUnmounted } from 'vue'


export function formatArmorType(armorType) {
    if (armorType === 'Cape') {
        return 'shoulder armor'
    } else {
        const arr = armorType.split(/(?=[A-Z])/)
        const lowerArr = arr.map(e => e.toLowerCase())
        const lowerStr = lowerArr.join(' ')
        
        return lowerStr;
    }
}

