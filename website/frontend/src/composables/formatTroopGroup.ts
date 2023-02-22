export default function fromatTroopGroup(troopGroup: string) {
    return (troopGroup === 'HorseArcher') ? 'horse archer' : troopGroup.toLowerCase()
}